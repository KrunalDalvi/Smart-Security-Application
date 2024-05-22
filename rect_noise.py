import cv2 

donel = False
doner = False
x1,y1,x2,y2 = 0,0,0,0


def select(event, x, y, flag, param):
    global x1,x2,y1,y2,donel, doner
    # To check if left mouse button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        x1,y1 = x,y 
        donel = True
    # To check if right mouse button was clicked    
    elif event == cv2.EVENT_RBUTTONDOWN:
        x2,y2 = x,y
        doner = True    
        print(doner, donel)

def rect_noise():

    global x1,x2,y1,y2, donel, doner
    #It lets you create a video capture object which is helpful to capture videos
    #through webcam and then you may perform desired operations on that video.
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("Select Region")
    # It will call the select function
    cv2.setMouseCallback("Select Region", select)

    while True:
        _, frame = cap.read() # Read() is used to read the frames 

        cv2.imshow("Select Region", frame)

        if cv2.waitKey(1) == 27 or doner == True:
            cv2.destroyAllWindows()
            print("gone--")
            break

    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()

        frame1only = frame1[y1:y2, x1:x2]
        frame2only = frame2[y1:y2, x1:x2]
        
        # Finds the absolute difference between background and current frame
        diff = cv2.absdiff(frame2only, frame1only)

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
            cv2.rectangle(frame1, (x+x1, y+y1), (x+w+x1, y+h+y1), (0,255,0), 2)
            # Display Text inside the frame 2 is for the thickness, (0, 255, 2) is the color
            cv2.putText(frame1, "MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 2)

        else:
            cv2.putText(frame1, "NO-MOTION", (10,80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2)

        cv2.rectangle(frame1, (x1,y1), (x2, y2), (0,0,255), 1)
        # Displaying the image/frame 
        cv2.imshow("Press Esc to Exit", frame1)

        # Display a frame for 1 ms, after which display will be automatically closed, 27 is wait for ESC key to exit
        if cv2.waitKey(1) == 27:
            cap.release() # When everything done, release the capture
            cv2.destroyAllWindows() # Forces to close all the open window
            break
 
