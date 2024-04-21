from base import Robot
import curses
import time
from picamera import PiCamera
import RPi.GPIO as GPIO

cam = PiCamera()
cam.resolution = (1280, 720)
cam.framerate = 25

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
time.sleep(1)
GPIO.cleanup()
r = Robot()

try:
    while True:
        char = screen.getch()
        if char == ord ('q'):
            break
        elif char == ord('r'):
            print('Recording..')
            cam.start_recording('/home/pi/Videos/record.h264', format='h264')
        elif char == ord('s'):
            print('Stop recording..')
            cam.stop_recording()
        elif char == curses.KEY_UP:
            r.forward()
        elif char == curses.KEY_DOWN:
            r.backward()
        elif char == curses.KEY_LEFT:
            r.left()
        elif char == curses.KEY_RIGHT:
            r.right()
        elif char == 32: # space bar
            r.stop()
        
finally:
    r.clean()
    cam.stop_recording()
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    
