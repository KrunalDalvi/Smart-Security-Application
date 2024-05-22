import cv2 

def noise():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()

        # Finds the absolute difference between background and current frame
        diff = cv2.absdiff(frame2, frame1)
        
        # Using cv2.COLOR_BGR2GRAY color space and it performs color space conversion for an image
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) 

        # It helps to blur an image
        diff = cv2.blur(diff, (5,5))
        # Thresholding used for separating an object considered as a foreground from its background
        # Threshold the diff image so that we get the foreground
        # threshold(source(must be grayscale),
        # thresholdValue(Value of Threshold below and above which pixel values will change accordingly),
        # maxVal(max value assigned to a pixel), thresholdingTechnique) 
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

       # Get the contours in the thresholded image
        # Contours are defined as the line joining all the points along the boundary of an image that are having the same intensity.
        # It works best on binary images, so we should first apply thresholding techniques.
        contr, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        if len(contr) > 0:
            # Based on contour area, get the maximum contour.
            max_cnt = max(contr, key=cv2.contourArea)
            x,y,w,h = cv2.boundingRect(max_cnt)
            # rectangle(image, start_point, end_point, color, thickness)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2) 
            cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)

        else:
            # Display Text inside the frame 2 is for the thickness, (0, 255, 2) is the color
            cv2.putText(frame1, "NO-MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2) 

        # Displaying the image/frame 
        cv2.imshow("Press ESC Key to Exit", frame1)

        # Display a frame for 1 ms, after which display will be automatically closed, 27 is wait for ESC key to exit
        if cv2.waitKey(1) == 27:  
            cap.release() # When everything done, release the capture
            cv2.destroyAllWindows()   # Forces to close all the open window
            break

