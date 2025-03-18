import cv2, os

####
# Daniel GV
###

def process_video(PATH_IN, PATH_OUT, WIDTH, HEIGHT):
    '''
    Procesa el video para apple.lsp
    '''
    cap = cv2.VideoCapture(PATH_IN)
    
    if not os.path.exists(PATH_OUT):
        os.makedirs(PATH_OUT)
    
    output_file = os.path.join(PATH_OUT, "frames.lsp")
    with open(output_file, "w") as f:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # funciones init
            f.write("(set_white)\n")
            f.write("(cls)\n")
            f.write("(setq deltatime (get-internal-real-time))\n")
            f.write(f"(move 0 {demo_y})\n")

            # Asegurarse solo blanco y negro
            frame = cv2.resize(frame, (WIDTH, HEIGHT), interpolation=cv2.INTER_NEAREST_EXACT)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            
            #funcion de pintado
            paint = lambda x: f"(drawrel {x} 0)"

            ## Optimiza pintando lineas del mismo color
            for row in bw:
                prev_pixel = None
                count = 0
                line = ""
                for pixel in row:
                    if pixel != prev_pixel:
                        if prev_pixel is not None:
                            line += paint(count)
                        line += "(set_white)" if pixel == 255 else "(set_black)"
                        count = 1
                    else:
                        count += 1
                    prev_pixel = pixel

                line += paint(count) + f"(moverel {-demo_x} -1)"
                f.write(f"{line}\n")

                
            # Espera dinamica del frame actual
            # framewait se define en apple.lsp
            f.write(f"(sleep (- framewait (/ (- (get-internal-real-time) deltatime) internal-time-units-per-second)))\n")            
    cap.release()

if __name__ == "__main__":
    # Uso
    demo_path_in = "video.mp4"
    demo_path_out = "output_frames"
    demo_x, demo_y = 400, 300
    process_video(demo_path_in, demo_path_out, demo_x, demo_y)
