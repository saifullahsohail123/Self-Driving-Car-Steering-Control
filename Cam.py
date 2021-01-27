import cv2
import numpy as np

#flags = [color for color in dir(cv2) if color.startswith('COLOR_')]
#print flags

cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
vid = cv2.VideoWriter('output.avi', fourcc, 6, (64,64))

counts = 0
countf = 0

while(True):
    tf, frame = cam.read()
    #print tf
    key = cv2.waitKey(1)
    Raw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #upper_red = np.array([130,255,255])
        #lower_red = np.array([110,100,100])
        #mask = cv2.inRange(frame, lower_red, upper_red)
        #frame = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('Single Frame', Raw) 
    
    if key == 27: #esc key
        break
    elif key == ord('w'):
        print ("You have pressed the letter w")
        Forward = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #upper_red = np.array([130,255,255])
        #lower_red = np.array([110,100,100])
        #mask = cv2.inRange(frame, lower_red, upper_red)
        #frame = cv2.bitwise_and(frame,frame, mask=mask)

        cv2.imshow('Single Frame', Forward)
        cv2.imwrite("forward{}.png".format(countf), Forward)
        countf+=1
    elif key == ord('s'):
        print ("You have pressed the letter s")
        Stop = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Single Frame', Stop)
        cv2.imwrite("stop{}.png".format(counts), Stop)
        counts +=1
    

cam.release()
vid.release()
cv2.destroyAllWindows()
