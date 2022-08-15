import paho.mqtt.client as mqtt
from time import sleep
import RPi.GPIO as GPIO 
led_verde = 20 #BCM

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(led_verde, GPIO.OUT, initial=GPIO.LOW) 

## Configuracion de servidor 
# servidor_ip = "192.168.0.20" ## Para publicar en otro dispositivo
servidor_ip = "localhost"   ## Para publicar a nuestro dispositivo
puerto=1883
cliente='Penguin'

## Creacion de TOPICS
topic1 = "mesa99/led/verde"

#Funciones 
def on_message(client, userdata, message):
    print("Mensaje recibido=", str(message.payload.decode("utf-8")))
    print("Topic=", message.topic)

client = mqtt.Client(cliente) 
client.on_message = on_message 
client.connect(servidor_ip, puerto) 
client.subscribe(topic1) # Subscripción al topic
client.loop_forever()