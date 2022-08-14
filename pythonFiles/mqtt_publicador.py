import paho.mqtt.client as mqtt

## Configuracion de servidor 
servidor_ip = "192.168.0.27" ## Para publicar en otro dispositivo
#servidor_ip = "localhost"   ## Para publicar a nuestro dispositivo
puerto=1883
cliente='Publicador_Penguin'

## Conexion al Servidor 
client = mqtt.Client(cliente) # Creación del cliente
client.connect(servidor_ip,puerto)

## Creacion de TOPICS
topic = "casa/luz"

client.publish(topic, "Ejemplo desde Python")