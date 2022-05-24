import Adafruit_DHT  # Libreria para uso de sensor
import RPi.GPIO as GPIO 
import time  

LED_Azul = 16 # GPIO 16
LED_Rojo = 20 # GPIO 20
LED_Verde = 21# GPIO 21

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_Azul , GPIO.OUT)
GPIO.setup(LED_Rojo , GPIO.OUT) 
GPIO.setup(LED_Verde, GPIO.OUT) 

while True:
    sensor = Adafruit_DHT.DHT11 
    pin = 12 # Pin de conexion del sensor
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    print (type(Adafruit_DHT.read_retry(sensor, pin)))
    print(Adafruit_DHT.read_retry(sensor, pin)[0])

    print ('Humedad: ' , humedad)
    print ('Temperatura: ' , temperatura)
    
    if temperatura> 28:
        GPIO.output(LED_Rojo, GPIO.HIGH) 
        GPIO.output(LED_Verde, GPIO.LOW) 
        GPIO.output(LED_Azul, GPIO.LOW) 

    elif temperature <28:
        GPIO.output(LED_Rojo, GPIO.LOW) 
        GPIO.output(LED_Verde, GPIO.LOW) 
        GPIO.output(LED_Azul, GPIO.HIGH) 
    else:
        GPIO.output(LED_Rojo, GPIO.LOW) 
        GPIO.output(LED_Verde, GPIO.HIGH) 
        GPIO.output(LED_Azul, GPIO.LOW)
    
    time.sleep(5)  # pausa de 5 segunos 
