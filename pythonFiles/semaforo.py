import RPi.GPIO as GPIO # Libreria para manejo de pines 
import time

# Los Pines de conexion GPIO 16, GPIO 20, GPIO 21
LED_Azul = 16
LED_Rojo = 20
LED_Verde = 21

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_Azul , GPIO.OUT)
GPIO.setup(LED_Rojo , GPIO.OUT) 
GPIO.setup(LED_Verde, GPIO.OUT) 

# Funcion para encender Led Amarillo
def encenderledAmarilo():
    GPIO.output(LED_Rojo, GPIO.HIGH) 
    GPIO.output(LED_Verde, GPIO.HIGH)
    GPIO.output(LED_Azul, GPIO.HIGH) 
    
# Funcion para apagar Led Amarillo
def apargarledAmarillo():
    GPIO.output(LED_Rojo, GPIO.LOW) 
    GPIO.output(LED_Verde, GPIO.LOW)
    GPIO.output(LED_Azul, GPIO.LOW) 


    
while True:
    ## Rojo
    GPIO.output(LED_Rojo, GPIO.HIGH) 
    time.sleep(1) 
    GPIO.output(LED_Rojo, GPIO.LOW) 
    time.sleep(1)
    
    ## Amarillo
    apargarledAmarillo()
    time.sleep(2)
    apargarledAmarillo()
    time.sleep(2)

    ## Verde  
    time.sleep(3)
    GPIO.output(LED_Verde, GPIO.HIGH) 
    time.sleep(3) 
    GPIO.output(LED_Verde, GPIO.LOW) 
    time.sleep(3)