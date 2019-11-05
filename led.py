import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

counter = 0
time.sleep = 1
try:
    while counter < 30:
        print("Led 1 on")
        GPIO.output(18,GPIO.HIGH)
        time.sleep
        print("Led off")
        GPIO.output(18,GPIO.LOW)
        time.sleep
        print("Kaut kas jauns")
        counter = counter + 1
        time.sleep = time.sleep - 0.09
except KeyboardInterrupt:
        print("/n"), counter
finally:
            GPIO.cleanup()