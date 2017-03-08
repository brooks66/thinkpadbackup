;; scheme daily homework 6
;; name: Nikolas Dean Brooks
;; date: February 8th, 2017

;; notice the use of debugging traps finally!!
(use-modules (ice-9 debugging traps) (ice-9 debugging trace))

(define sum*
 (lambda (ttup)
  (cond
   ((null? ttup) 0) ;; Nothing is provided/base case
    ((null? (cdr ttup)) (car (car ttup))) ;; If no children
     (else(+(sum* (car(cdr ttup)))(sum* (cons (car ttup) (cdr (cdr ttup))))))
  )
 )
)


;(install-trap (make <procedure-trap>
 ;                           #:procedure sum*
  ;                          #:behaviour (list trace-trap trace-until-exit)))

;; tests!
(display (sum* '((5)) ))
(display "\n")

(display (sum* '((0) ((0) ((5))) ((0) ((10)))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7)))) ((0) ((10) ))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7) ) ((8) ))) ((0) ((10) ))) ))
(display "\n")

;; correct output:
;;   $ guile d6.scm
;;   5
;;   15
;;   22
;;   30

