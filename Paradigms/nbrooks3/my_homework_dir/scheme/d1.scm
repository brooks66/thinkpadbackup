;; this is how to load external modules in scheme
(load-from-path "/home/scratch/paradigms/scheme_dailies/d1/paradigms_d1.scm")
(use-modules (ice-9 paradigms_d1))

;; Nikolas Dean Brooks

;; the list q
;; notice it has a ' in front of the list; that tells the interpreter to read
;; the list literally (e.g., as atoms, instead of functions)
(define q '(turkey (gravy) (stuffing potatoes ham) peas))

;; question 1
(display "question 1: ")
(display (atom? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; #f
;;
;; explanation:
;; The innermost cdr removes turkey, the second removes gravy.
;; The car command references the first thing of what's left
;; or in this case "(stuffing potatoes ham)".
;; "(stuffing potatoes ham)" is not an atom, so the output
;; was "false" (#f).


;; question 2
(display "question 2: ")
(display (lat? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; #t
;;
;; explanation:
;; Similar to above, we're left with "(stuffing potatoes ham)"
;; It is a list of atoms, so we get the output of true (#t).


;; question 3
(display "question 3: ")
(display (cond ((atom? (car q)) (car q)) (else '())))
(display "\n")
;; output:
;; turkey
;;
;; explanation:
;; (be sure to describe what cond and else do from the perspective
;;   of the theory we discussed in class; googling will mislead you.)
;;
;; cond looks to a condition and if the condition is true
;; will print the thing to the right of the closed condition
;; In this case, it looks at (atom? (car q)). car q is turkey,
;; which is an atom. Because atom? evaluated to true, it
;; prints (car q), which is "turkey".

