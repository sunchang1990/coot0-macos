
(define results '())
(define (check name thunk)
  (let ((r (catch #t
             (lambda () (let ((v (thunk))) (list name (if v 'PASS 'FAIL) v)))
             (lambda (key . args) (list name 'FAIL (format #f "EXC ~s ~s" key (if (pair? args) (car args) args)))))))
    (set! results (cons r results))))
(define imol (import-rdkit-mol-from-smiles "CCO" "ETH"))   ; ethanol: 3 heavy atoms + 6 H
(check "import-rdkit-mol-from-smiles (ethanol) gives a model molecule" (lambda () (and (>= imol 0) (valid-model-molecule? imol))))
(check "ethanol has 9 atoms (C2 H6 O)" (lambda () (= (length (residue-info imol (car (chain-ids imol)) 1 "")) 9)))
(check "bad SMILES returns -1" (lambda () (= (import-rdkit-mol-from-smiles "C1CC(" "BAD") -1)))
(for-each (lambda (r) (format #t "~a ~a~a~%" (if (eq? (cadr r) 'PASS) "PASS" "FAIL") (car r) (if (eq? (cadr r) 'PASS) "" (format #f "  => ~s" (caddr r))))) (reverse results))
(format #t "SUMMARY ~a / ~a~%" (length (filter (lambda (r) (eq? (cadr r) 'PASS)) results)) (length results))
(coot-real-exit 0)
