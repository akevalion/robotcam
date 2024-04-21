import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
for x in range(1, 10):
    GPIO.output(7, True)
    time.sleep(0.1)
    GPIO.output(7, False)
    time.sleep(0.1)
    
GPIO.cleanup()