import paho.mqtt.client as mqtt
import Adafruit_DHT  # Libreria para uso de sensor
from time import sleep

## Configuracion de servidor 
# servidor_ip = "192.168.100.XXX" ## Para publicar en otro dispositivo
servidor_ip = "localhost"   ## Para publicar a nuestro dispositivo
puerto=1883
cliente='Penguin'

## Conexion al Servidor 
client = mqtt.Client(cliente) # Creacion del cliente
client.connect(servidor_ip,puerto)

## Creacion de TOPICS
topic1 = "mesa99/sensor/humedad"
topic2 = "mesa99/sensor/temperatura"

## Publicacion
while True:
    sensor = Adafruit_DHT.DHT11 
    pin = 12 # Pin de conexion del sensor
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    client.publish(topic1, str(humedad))
    delay(5)
    client.publish(topic2, str(temperatura))
    delay(5)
