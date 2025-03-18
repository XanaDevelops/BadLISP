(load 'sleep)


; Funciones de color
(defun set_white()
    (color 255 255 255)
)
(defun set_black ()
    (color 0 0 0)
)

(defun main()
    (princ "BAD APPLE\n")
    (print 3)
    (sleep 1)
    (print 2)
    (sleep 1)
    (print 1)
    (sleep 1)
    (drawt)
    (terpri)
)


(defun drawt()
    (cls)
    (load 'output_frames/frames) 
)

(setq framewait 0.03095) ;Magic value para sync con el video de yt, requiere mayor precisión (siempre se puede poner "1/30")
(main)
