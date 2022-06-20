#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO # Libreria para manejo de GPIO
import time

LED_Amarillo = 16 # GPIO 16
LED_Rojo = 20 # GPIO 20
LED_Verde = 21# GPIO 21

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_Amarillo , GPIO.OUT)
GPIO.setup(LED_Rojo , GPIO.OUT) 
GPIO.setup(LED_Verde, GPIO.OUT) 

 
while True:
    
    GPIO.output(LED_Amarillo, GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(LED_Amarillo, GPIO.LOW) 
    time.sleep(1)
    
    GPIO.output(LED_Rojo, GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(LED_Rojo, GPIO.LOW) 
    time.sleep(1)
    
    GPIO.output(LED_Verde, GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(LED_Verde, GPIO.LOW) 
    time.sleep(1)