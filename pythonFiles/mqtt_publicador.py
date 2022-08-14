import paho.mqtt.client as mqtt

servidor_ip = "localhost"
puerto=1883
client = mqtt.Client('Publicador_ejem1') # Creación del cliente
client.connect(servidor_ip,puerto)
topic = "casa/luz"

client.publish(topic, "Ejemplo desde Python")