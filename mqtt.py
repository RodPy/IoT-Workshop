
from paho.mqtt import client as mqtt_client

import random
import time
broker = '192.168.0.3'
port = 1883
topic = "rele1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

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
        
        result = client.publish(topic, msg)
        print (result)
        
        status = result[0] # 0 cuando logra enviar
        if status == 0:
            print(f"Enviando `{msg}` al topic `{topic}`")
        else:
            print(f"Mensaje no enviado al topic -> {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()

