import RPi.GPIO as GPIO

class Robot:
    def __init__(self):
        self.pleftF = 7
        self.pleftB = 11
        self.prightF = 18
        self.prightB = 16
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pleftF, GPIO.OUT)
        GPIO.setup(self.pleftB, GPIO.OUT)
        GPIO.setup(self.prightF, GPIO.OUT)
        GPIO.setup(self.prightB, GPIO.OUT)

    def leftFOn(self):
        GPIO.output(self.pleftF, True)

    def leftFOff(self):
        GPIO.output(self.pleftF, False)

    def leftBOn(self):
        GPIO.output(self.pleftB, True)

    def leftBOff(self):
        GPIO.output(self.pleftB, False)

    def rightFOn(self):
        GPIO.output(self.prightF, True)
    
    def rightFOff(self):
        GPIO.output(self.prightF, False)
    
    def rightBOn(self):
        GPIO.output(self.prightB, True)

    def rightBOff(self):
        GPIO.output(self.prightB, False)
    
    def clean(self):
        GPIO.cleanup()
        
    def forward(self):
        self.rightBOff()
        self.leftBOff()
        self.rightFOn()
        self.leftFOn()
        
    def backward(self):
        self.rightFOff()
        self.leftFOff()
        self.rightBOn()
        self.leftBOn()
        
    def left(self):
        self.rightBOff()
        self.leftFOff()
        self.rightFOn()
        self.leftBOn()
        
    def right(self):
        self.leftBOff()
        self.rightFOff()
        self.leftFOn()
        self.rightBOn()
        
    def stop(self):
        self.rightFOff()
        self.rightBOff()
        self.leftFOff()
        self.leftBOff()