import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(4, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)
try:
    while True:
        button_state1 = GPIO.input(4)
        button_state2 = GPIO.input(18)
        button_state3 = GPIO.input(23)
    if button_state1 == GPIO.LOW:
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(0.5)
    
        

        
    else :
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:
        print("/n"), counter
finally:
            GPIO.cleanup()
    

        