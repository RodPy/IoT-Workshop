import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 
import time

## Configuracion de servidor 
# servidor_ip = "192.168.0.20" ## Para publicar en otro dispositivo
servidor_ip = "localhost"   ## Para publicar a nuestro dispositivo
puerto=1883
cliente='Penguin'


## Creacion de TOPICS
topic1 = "mesa99/led/rojo"
topic2 = "mesa99/led/verde"
topic3 = "mesa99/led/amarillo"

# GIPIO
led_verde = 20 #BCM
led_rojo = 21 #BCM
led_amarillo = 16 #BCM

# Setting up the GPIO pins.
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(led_verde, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(led_rojo, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(led_amarillo, GPIO.OUT, initial=GPIO.LOW) 


#Funciones 
def on_message(client, userdata, message):
    print("Mensaje recibido=", str(message.payload.decode("utf-8")))
    print("Topic=", message.topic)

   # Decoding the message and assigning it to the variable `msj` and assigning the topic to the
   # variable `topico`.
    msj=str(message.payload.decode("utf-8"))
    topico= message.topic

    # Checking the topic and message and then turning on or off the leds.
    if topico==topic1 and msj=='ON':
        GPIO.output(led_verde, GPIO.HIGH) 
        time.sleep(1) 
    elif topico==topic1 and msj=='OFF':   
        GPIO.output(led_verde, GPIO.LOW) 
        time.sleep(1)
    
    if topico==topic2 and msj=='ON':
        GPIO.output(led_rojo, GPIO.HIGH) 
        time.sleep(1) 
    elif topico==topic2 and msj=='OFF':   
        GPIO.output(led_rojo, GPIO.LOW) 
        time.sleep(1)
    
    if topico==topic3 and msj=='ON':
        GPIO.output(led_amarillo, GPIO.HIGH) 
        time.sleep(1) 
    elif topico==topic3 and msj=='OFF':   
        GPIO.output(led_amarillo, GPIO.LOW) 
        time.sleep(1)

# Creating a client object.
client = mqtt.Client(cliente) 

# Assigning the function `on_message` to the `on_message` event of the `client` object.
client.on_message = on_message 

# Connecting to the MQTT broker.
client.connect(servidor_ip, puerto) 

client.subscribe(topic1) # Subscripción al topic
client.subscribe(topic2) # Subscripción al topic
client.subscribe(topic3) # Subscripción al topic

# A blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()

