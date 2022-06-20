
from paho.mqtt import client as mqtt_client
import random
import time

broker = '172.20.10.3'
port = 1883

## Topic 
bano = "rele1"
sala = "rele2"
cocina = "rele3"
dormitorio = "rele4"
client_id = "RodPy"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado a MQTT Broker!")
        else:
            print("Conexion fallida,  code %d\n", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        if msg_count%2==0: msg="true"
        else : msg ="false"
        result = client.publish(bano, msg)
        print (result)        
        status = result[0] # 0 cuando logra enviar
        if status == 0:
            print(f"Enviando `{msg}` al topic `{bano}`")
        else:
            print(f"Mensaje no enviado al topic -> {bano}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()

