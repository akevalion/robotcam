from picamera import PiCamera
import time

cam = PiCamera()
cam.resolution = (1280, 720)
cam.framerate = 25

time.sleep(1)
cam.start_recording('/home/pi/Videos/foo.h264', format='h264')
time.sleep(5)
cam.stop_recording()