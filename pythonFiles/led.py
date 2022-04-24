
import RPi.GPIO as GPIO 
import time

LED_PIN = 2
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW) 


while True:
    GPIO.output(LED_PIN, GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(LED_PIN, GPIO.LOW) 
    time.sleep(1)