;; scheme daily homework 3
;; name: Nikolas Dean Brooks
;; date: January 30th, 2017

(load-from-path "/home/scratch/paradigms/scheme_dailies/d3/paradigms_d3.scm")
(use-modules (ice-9 paradigms_d3))

;; double
(define double 
  (lambda (n)
    (cond
      ((zero? n) n)
	(else (add1 (add1 (double (sub1 n))))))))
    ;; right now double always returns the same number given to it
    ;; make it return *double* that number
    ;; remember that ``number'' means positive integer, for now
    ;; use *only* the functions add1, sub1, and zero?
    ;; do *not* use +, -, *, /, etc.

;; tests!
(display (double 9))
(display "\n")

(display (double 2))
(display "\n")

(display (double 45))
(display "\n")

;; correct output:
;;   $ guile d3.scm
;;   18
;;   4
;;   90

