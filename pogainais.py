import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

counter = 0
laiks = 1.4
try:
    while counter < 100:
        button_state = GPIO.input(4)
    if button_state == GPIO.HIGH:
        print ("poga1_HIGH")
        GPIO.output(17,GPIO.HIGH)
        time.sleep(laiks)
        GPIO.output(17,GPIO.LOW)
        time.sleep(laiks)
        counter = counter + 1
        laiks = laiks - 0.01

        
    else :
        print("poga1_LOW")
        GPIO.output(17,GPIO.LOW)
except KeyboardInterrupt:
        print
    
finally:
            GPIO.cleanup()
        