import cv2
import numpy as np
import datetime

def track_people():
    #It lets you create a video capture object which is helpful to capture videos
    #through webcam and then you may perform desired operations on that video.
    cap = cv2.VideoCapture(0)

    #taking input point
    _, inp_img = cap.read()
    
    # flip() is used to flip a 2D array
    # positive value (for example, 1) means flipping around y-axis
    inp_img = cv2.flip(inp_img, 1)
    # It helps to blur an image which is of (4,4) kernel size
    inp_img = cv2.blur(inp_img, (4,4))

    # Using cv2.COLOR_BGR2GRAY color space and it performs color space conversion for an image
    gray_inp_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)

    # tracking starts here 
    old_pts = np.array([[350, 180], [350, 350]], dtype=np.float32).reshape(-1,1,2)

    # Creating backup of the starting points.
    backup = old_pts.copy()
    backup_img = gray_inp_img.copy()

    # text output window with 3 channels
    # which will display and tell us whether someone has entered or exit the frame
    outp = np.zeros((480,640,3))

    ytest_pos = 40

    while True:
        # Read() is used to read the frames
        _, new_inp_img = cap.read()
        new_inp_img = cv2.flip(new_inp_img, 1)
        # It helps to blur an image
        new_inp_img = cv2.blur(new_inp_img, (4,4))
        # Using cv2.COLOR_BGR2GRAY color space and it performs color space conversion for an image
        new_gray = cv2.cvtColor(new_inp_img, cv2.COLOR_BGR2GRAY)
        # calcOpticalFlowPyrLK()is used to track certain points on a video
        # cv2.calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, nextPts, winSize, maxLevel(if set to 1, two levels are used),
        # criteria(specifying the termination criteria of the iterative search algorithm))
        new_pts,status,err = cv2.calcOpticalFlowPyrLK(gray_inp_img, 
                             new_gray, 
                             old_pts, 
                             None, maxLevel=1,
                             criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,
                                                         15, 0.08))
        
        # Creating boundries for the points which we are tracking
        # It prevents the points to go out of the window
        # The x value will not exceed 600 and y value will not exceed 350
        # Ravel() is used to change a 2-dimensional array or a
        # multi-dimensional array into a contiguous flattened array(1D Array)
        # The returned array has the same data type as the source array or input array.
        if new_pts.ravel()[0] >= 600:
            new_pts.ravel()[0] = 600
        if new_pts.ravel()[1] >= 350:
            new_pts.ravel()[1] = 350
        if new_pts.ravel()[0]  <= 20:
            new_pts.ravel()[0] = 20
        if new_pts.ravel()[1] <= 150:
            new_pts.ravel()[1] = 150
        if new_pts.ravel()[2]  >= 600:
            new_pts.ravel()[2] = 600
        if new_pts.ravel()[3] >= 350:
            new_pts.ravel()[3] = 350
        if new_pts.ravel()[2]  <= 20:
            new_pts.ravel()[2] = 20
        if new_pts.ravel()[3] <= 150:
            new_pts.ravel()[3] = 150

        # Converting it into a 1D array and
        # then storing the values in a, b, x and y   [ x y    -> The value in postion of x will be stored in x 
        #                                              a b ]
        x,y = new_pts[0,:,:].ravel()
        a,b = new_pts[1,:,:].ravel()
        # line() method is used to draw a line on any image
        # x, y are starting coordinates and a, b are ending coordinates and 15 is the width
        cv2.line(new_inp_img, (int(x),int(y)), (int(a),int(b)), (0,0,255), 15)
    
        # imshow() is used to display an image in a window
        cv2.imshow("Track", new_inp_img)

        # if the x value is > 400 and 550 then it will print gone at with time and reset the new points and image
        # if the x value is between the 400 and 550 then it won't print gone at
        if new_pts.ravel()[0]  > 400 or new_pts.ravel()[2]  > 400:        
            if new_pts.ravel()[0] > 550 or new_pts.ravel()[2]  > 550:
                new_pts = backup.copy()
                new_inp_img = backup_img.copy()
                ytest_pos += 40
                cv2.putText(outp, "Gone at {}".format(datetime.datetime.now().strftime("%H:%M")), (10,ytest_pos), 
                    cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0))

        # if the x value is < 200 and 50 then it will print came at with time and reset the new points and image
        # if the x value is between the 200 and 50 then it won't print came at
        elif new_pts.ravel()[0]  < 200 or new_pts.ravel()[2]  < 200:        
            if new_pts.ravel()[0] < 50 or new_pts.ravel()[2]  < 50:
                new_pts = backup.copy()
                new_inp_img = backup_img.copy()
                ytest_pos += 40
                cv2.putText(outp, "Came at {}".format(datetime.datetime.now().strftime("%H:%M")), (10,ytest_pos), 
                    cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255))

        # imshow() is used to display an image in a window
        cv2.imshow('Display Output', outp)
        # Updates the new value in old image and points
        gray_inp_img = new_gray.copy()
        old_pts = new_pts.reshape(-1,1,2)

        if cv2.waitKey(1) & 0xff == 27:
            break
    
    cv2.destroyAllWindows()
    cap.release()


# nextPts – output vector of 2D points (with single-precision floating-point coordinates) containing the
#calculated new positions of input features in the second image.

# status – output status vector (of unsigned chars); each element of the vector is set to 1 if the flow
#for the corresponding features has been found, otherwise, it is set to 0.

# err – output vector of errors; each element of the vector is set to an error for the corresponding
# feature, type of the error measure can be set in flags parameter. If the flow wasn’t found then the
# error is not defined (use the status parameter to find such cases).
