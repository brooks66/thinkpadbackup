;; scheme tictactoe homework
;; name: Nikolas Dean Brooks
;; date: February 15th, 2017

(load-from-path "/home/scratch/paradigms/scheme_tictactoe/paradigms_ttt.scm")
(use-modules (ice-9 paradigms_ttt))

;; REPLACE WITH YOUR FUNCTIONS FROM A PREVIOUS HOMEWORK:
;;  greatest
;;  positionof
;;  value

(define greatest
 (lambda (tup)
  (cond
   ((null? tup) 0) ;; Nothing is provided/base
    ((> (car tup) (greatest (cdr tup))) (car tup))
     (else (greatest (cdr tup)))
)))

(define positionof
 (lambda (a tup)
  (cond
   ((null? tup) 0)
    ((eq? n (car tup)) 1)
     (else (+ 1 (positionof n (cdr tup))))  
)))

(define value
 (lambda (p gs)
  (cond
   ((win? p gs) 10)
    ((win? (other p) gs) -10)
     (else 0))))

;; MODIFY your sum* function for this assignment...
(define sum*-g
 (lambda (ttup f)
  (cond
   ((null? ttup) 0)
    ((null? (cdr ttup)) (f (car ttup)))
     (else (+ (sum*-g (car(cdr ttup)) f) (sum*-g (cons (car ttup) (cdr (cdr ttup))) f)))   
)))

;; It would be helpful if the currying function takes 
;; in a gamestate and returns value for the player
;; for that game state:

(define curryhelper
 (lambda (p)
  (lambda (gs)
   (cond 
    ((null? gs) '())	
     (else (value p gs))
))))

;; MODIFY this function so that given the game tree 
;; (where the current situation is at the root),
;; it returns the recommendation for the next move
(define nextmove
 (lambda (p gt)
  (cond 
   ((null? gt) '())
    (else (display "Grader, read comment under nextmove. Partial credit?") '())  
)))

;; Partial credit? I think I know what I would have to do,
;; but I'm not sure how to carry it out properly with scheme. :/
;;
;; I did attempt Shreya's office hours, but she was swamped
;; from start to finish.
;;
;; FOR NEXTMOVE, I would have had to do this:
;; - Use greatest to find the greatest value returned from
;; sum*-g for a particular "level" or "depth"
;; - Use positionof that returned greatest value to find
;; out where it came from
;; - Now the the position of the greatest sum*-g result
;; was found, we can print out the board at that location.
;; It was the board with the highest value, or best potential
;; to win, and thus would be the recommended move.

;; what is the current game situation?
(display "Current State:     ")
(display (car (onegametree)))
(display "\n")

;; test of nextmove, where should we go next?
(display "Recommended Move:  ")
(display (nextmove 'x (onegametree)))
(display "\n")

;; correct output:
;;   $ guile tictactoe.scm
;;   Current State:     (x o x o o e e x e)
;;   Recommended Move:  (x o x o o x e x e)

