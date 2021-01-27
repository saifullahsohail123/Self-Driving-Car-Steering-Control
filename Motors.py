import RPi.GPIO as io
import time
import cv2
from unicurses import *

io.setwarnings(False)
io.setmode(io.BOARD)

in1_pin1=7
in2_pin1=11
in1_pin2=13
in2_pin2=15

io.setup(in1_pin1,io.OUT)
p1=io.PWM(in1_pin1,50)
p1.start(0)

io.setup(in2_pin1,io.OUT)
p2=io.PWM(in2_pin1,50)
p2.start(0)

io.setup(in1_pin2,io.OUT)
p3=io.PWM(in1_pin2,50)
p3.start(0)

io.setup(in2_pin2,io.OUT)
p4=io.PWM(in2_pin2,50)
p4.start(0)

screen=initscr()
curses.noecho()
curses.cbreak()
key.keypad(True)

def forward():
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(50)
    time.sleep(2)
    main()
def backward():
    p1.start(0)
    p2.start(0)
    p3.start(50)
    p4.start(0)
    time.sleep(2)
    
def right():
    p1.start(0)
    p2.start(100)
    p3.start(0)
    p4.start(0)
    time.sleep(2)
    
def left():
    p1.start(100)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    time.sleep(2)
    
def stop():
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    time.sleep(4)

cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
vid = cv2.VideoWriter('output.avi', fourcc, 6, (64,64))

'''
while True:
    key = cv2.waitKey(1) & 0xFF
    
    if key==ord('w'):
        print('forward')
    elif key == 27:
        cv2.destroyAllWindows()
        break
'''
def main():
    while(True):
        tf, frame = cam.read()
        #print tf
        #stop()
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
            forward()
            
        elif key == ord('s'):
            print ("You have pressed the letter s")
            stop()

    cam.release()
    vid.release()
    cv2.destroyAllWindows()
while(True):
    char=screen.getch()
    if char == ord('q'):
        break
    elif char == curses.KEY_UP:
        print ("You have pressed the letter w")
        forward()






