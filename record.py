import cv2
from datetime import datetime

def record():
    #It lets you create a video capture object which is helpful to capture videos
    #through webcam and then you may perform desired operations on that video.
    cap = cv2.VideoCapture(0)
    
    # VideoWriter() is used to save a recorded video,
    # FourCC is a 4-byte code used to specify the video codec,
    # The codecs for Windows is DIVX,
    # FourCC code is passed as  cv2.VideoWriter_fourcc(*’XVID’) for DIVX.
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    
    # VideoWriter( filename, fourcc (Defining the codec), 
    # fps(defined frame rate of the output video stream),
    # frameSize(Size of the video frames))
    out = cv2.VideoWriter(f'recordings/{datetime.now().strftime("%H-%M-%S")}.avi', fourcc,20.0,(640,480))

    while True:
        _, frame = cap.read() # Read() is used to read the frames
        
        # Display Text inside the frame 2 is for the thickness, (0, 255, 2) is the color
        cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50,50), cv2.FONT_HERSHEY_COMPLEX,
                        0.6, (255,255,255), 2)

        # Inserts the string in a single line in the file.
        out.write(frame)
        
        # Displaying the image/frame 
        cv2.imshow("Record: Press ESC to Stop", frame)

        # Display a frame for 1 ms, after which display will be automatically closed, 27 is wait for ESC key to exit 
        if cv2.waitKey(1) == 27:
            cap.release() # When everything done, release the capture
            cv2.destroyAllWindows() # Forces to close all the open window
            break 
