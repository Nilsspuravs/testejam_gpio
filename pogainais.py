import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button = 4

GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

while True:
    button_state = GPIO.input(button)
    if button_state == GPIO.HIGH:
        print ("poga1_HIGH")
        time.sleep(1)
    else:
        print("poga1_LOW")
        time.sleep(1)