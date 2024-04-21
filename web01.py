from flask import Flask, request, render_template, send_file
import requests
from base import Robot
from datetime import datetime
from picamera import PiCamera
import RPi.GPIO as GPIO
import time

print("\n\n==LoadingCamera==\n\n")
cam = PiCamera()
cam.resolution = (500, 500)
cam.framerate = 25
time.sleep(1)
print("\n\n==LoadingServer==\n\n")
app = Flask(__name__)
GPIO.cleanup()
robot = Robot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forward')
def forward():
    robot.forward()
    return render_template('index.html')

@app.route('/back')
def backward():
    robot.backward()
    return render_template('index.html')

@app.route('/left')
def left():
    robot.left()
    return render_template('index.html')

@app.route('/right')
def right():
    robot.right()
    return render_template('index.html')

@app.route('/stop')
def stop():
    robot.stop()
    return render_template('index.html')

@app.route('/grabar')
def grabar():
    now = datetime.now()
    name = now.strftime("%Y%m%d_%H%M%S")
    cam.start_recording(f"/home/pi/Videos/Video{name}.h264", format="h264")
    return render_template('index.html')

@app.route('/pararGrabacion')
def pararGrabacion():
    cam.stop_recording()
    return render_template('index.html')


@app.route('/bg.png')
def image():
    return send_file('bg.png')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')