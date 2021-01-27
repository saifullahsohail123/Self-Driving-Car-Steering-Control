import RPi.GPIO as io
import time
import cv2
import getch
from pynput.keyboard import Key,Controller
from pygame import *

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


def left():
    p1.start(70)
    p2.start(0)
    p3.start(0)
    p4.start(100)
    
def right():
    p1.start(60)
    p2.start(0)
    p3.start(100)
    p4.start(0)
    
    
def backward():
    p1.start(0)
    p2.start(100)
    p3.start(0)
    p4.start(0)
   
    
def forward():
    p1.start(60)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    print('Forwarding')
    
def stop():
    p1.start(0)
    p2.start(0)
    p3.start(0)
    p4.start(0)
    

cam = cv2.VideoCapture(0)

'''
while True:
    key = cv2.waitKey(1) & 0xFF
    
    if key==ord('w'):
        print('forward')
    elif key == 27:
        cv2.destroyAllWindows()
        break
'''
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

'''

init()
screen = display.set_mode((320,40))
display.set_caption('SDC')

countf = 888
countr = 0
countl = 1010
countb = 0
FC=0
RC=0
LC=0
BC=0
endProgram =0

while(endProgram == 0):
    '''
    key=keyboard.press('Enter'(input('Enter'))
    
    if(key=='q'):
        print('q pressed')
        stop()
        break
    elif (key=='w'):
        forward()
    elif (key=='r'):
        right()
    '''
    tf, frame = cam.read()  
    Forward = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
    for e in event.get():
        if e.type == KEYDOWN:
            if(e.key == K_UP):
               forward()
               FC=1
               RC=0
               LC=0

            if(e.key == K_DOWN):
                stop()
                FC=0
                RC=0
                LC=0
                BC=1
                
            if(e.key == K_RIGHT):
                right()
                FC=0
                RC=1
                LC=0
    
            if(e.key == K_LEFT):
                left()
                FC=0
                LC=1
                RC=0
            if(e.key == K_ESCAPE):
                endProgram=1
            if(e.key == K_q):
                backward()
            else:
                print(e.key)
                
    if(FC == 1):
        cv2.imwrite("Fimages/forward{}.png".format(countf), Forward)
        countf+=1
        print('Saving Forward Pic ',countf)
    if(RC == 1):
       # cv2.imwrite("Fimages/right{}.png".format(countr), Forward)
       # countr+=1
        print('Saving Right Pic')
    if(LC==1):
       # cv2.imwrite("Fimages/left{}.png".format(countl), Forward)
       # countl+=1
        print('Saving Left Pic ', countl)
    if(BC == 1):
        cv2.imwrite("Bimages/forward{}.png".format(countb), Forward)
        countb+=1
        print('Saving Stop Pic ',countb)    
    

           
    
quit()
cam.release()
cv2.destroyAllWindows()
'''
    char=screen.getch()
    if char == ord('q'):
        break
    elif char == curses.KEY_UP:
        print ("You have pressed the letter w")
        forward()
    '''




