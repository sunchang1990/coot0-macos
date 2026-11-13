
(define results '())
(define (check name thunk)
  (let ((r (catch #t
             (lambda () (let ((v (thunk))) (list name (if v 'PASS 'FAIL) v)))
             (lambda (key . args) (list name 'FAIL (format #f "EXC ~s ~s" key (if (pair? args) (car args) args)))))))
    (set! results (cons r results))))
(define here (canonicalize-path (getenv "COOT_PREFIX")))
(define (inside? p) (and (string? p) (file-exists? p) (string-prefix? (string-append here "/") (canonicalize-path p))))
(format #t "LOAD-PATH ~s~%" %load-path)
(format #t "COMPILED-PATH ~s~%" %load-compiled-path)
(check "every existing %load-path entry is inside the bundle (or the cache)"
       (lambda () (every (lambda (p) (or (not (file-exists? p)) (inside? p) (string-prefix? (getenv "XDG_CACHE_HOME") p))) %load-path)))
(check "every existing %load-compiled-path entry is inside the bundle or the cache"
       (lambda () (every (lambda (p) (or (not (file-exists? p)) (inside? p) (string-prefix? (getenv "XDG_CACHE_HOME") p))) %load-compiled-path)))
(check "standard Guile modules load from the bundle (srfi-1, regex, threads, sxml, popen, rdelim, textual-ports)"
       (lambda () (use-modules (srfi srfi-1) (ice-9 regex) (ice-9 threads) (sxml simple) (ice-9 popen) (ice-9 rdelim) (ice-9 textual-ports)) #t))
;; (ice-9 readline) itself cannot find this extension: conda installs it as guile-readline.0.so, macOS Guile looks for .dylib.
;; That only affects line editing at Guile's interactive prompt, not Coot; what matters here is that the shipped extension dlopens from the bundle.
(check "guile extension library dlopens from the bundle (guile-readline.0.so)"
       (lambda () (dynamic-link (string-append here "/lib/guile/3.0/extensions/guile-readline.0.so")) #t))
(check "foreign function interface (libffi) calls into libc" (lambda () (use-modules (system foreign)) (pointer? (dynamic-func "strlen" (dynamic-link)))))
(check "coot-version" (lambda () (string? (coot-version))))
(for-each (lambda (r) (format #t "~a ~a~a~%" (if (eq? (cadr r) 'PASS) "PASS" "FAIL") (car r) (if (eq? (cadr r) 'PASS) "" (format #f "  => ~s" (caddr r))))) (reverse results))
(format #t "SUMMARY ~a / ~a~%" (length (filter (lambda (r) (eq? (cadr r) 'PASS)) results)) (length results))
(coot-real-exit 0)
