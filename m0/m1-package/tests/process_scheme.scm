
(define results '())
(define (check name thunk)
  (let ((r (catch #t
             (lambda () (let ((v (thunk))) (list name (if v 'PASS 'FAIL) v)))
             (lambda (key . args) (list name 'FAIL (format #f "EXC ~s ~s" key (if (pair? args) (car args) args)))))))
    (set! results (cons r results))))
(define tmp (string-append "/tmp/coot-proc-test-" (number->string (getpid))))
(check "run: exit 0 -> #t" (lambda () (eq? #t (run "true"))))
(check "run: exit 1 -> #f" (lambda () (eq? #f (run "false"))))
(check "goosh-command returns the exit status" (lambda () (eqv? 3 (goosh-command "sh" (list "-c" "exit 3") '() "/dev/null" #f))))
(check "goosh-command: stdout goes to the log file, stdin comes from data-list"
       (lambda ()
         (goosh-command "cat" '() (list "alpha" "beta") tmp #f)
         (equal? (call-with-input-file tmp (lambda (p) (list (read-line p) (read-line p)))) (list "alpha" "beta"))))
(check "goosh-command quotes arguments (spaces, quotes, ^, $)"
       (lambda ()
         (goosh-command "printf" (list "%s|" "a b" "it's" "^USER" "$HOME") '() tmp #f)
         (equal? (call-with-input-file tmp read-line) "a b|it's|^USER|$HOME|")))
(check "goosh-command: missing command -> 255 and no crash" (lambda () (eqv? 255 (goosh-command "no-such-command-xyz" '() '() tmp #f))))
(check "run-command/strings returns output lines in order"
       (lambda () (equal? (run-command/strings "printf" (list "one\ntwo\n") '()) (list "one" "two"))))
(check "run-command/strings feeds data-list to stdin"
       (lambda () (equal? (run-command/strings "cat" '() (list "x" "y")) (list "x" "y"))))
(check "goosh-command-with-file-input: input file -> log file"
       (lambda ()
         (let ((in (string-append tmp ".in")))
           (call-with-output-file in (lambda (p) (format p "from-file~%")))
           (goosh-command-with-file-input "cat" '() in tmp)
           (let ((ok (equal? (call-with-input-file tmp read-line) "from-file")))
             (delete-file in) ok))))
(check "a failing exec is reported by the shell, not silent"
       (lambda ()
         (let ((st (%system-status (string-append "exec " (%sh-quote "/tmp") " 2>" (%sh-quote tmp)))))
           (and (number? st) (> st 0)))))
(if (file-exists? tmp) (delete-file tmp))
(for-each (lambda (r) (format #t "~a ~a~%" (if (eq? (cadr r) 'PASS) "PASS" "FAIL") (car r))) (reverse results))
(format #t "SUMMARY ~a / ~a~%" (length (filter (lambda (r) (eq? (cadr r) 'PASS)) results)) (length results))
(coot-real-exit 0)
