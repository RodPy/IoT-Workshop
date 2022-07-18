from paho.mqtt import client as mqtt_client
import time

broker = '192.168.100.63'
port = 1883

## Topic 
bano = "rele1"
sala = "rele2"
cocina = "rele3"
dormitorio = "rele4"
client_id = "Penguin"

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


def publishone(client):
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

def publish(client,msg,topic):
    result = client.publish(topic, msg)
    print (result)        
    status = result[0] # 0 cuando logra enviar
    if status == 0:
        print(f"Enviando `{msg}` al topic `{topic}`")
    else:
        print(f"Mensaje no enviado al topic -> {topic}")

def run():
    client = connect_mqtt()
    client.loop_start()
    # publish(client)
    # publishone(client)

    while True:
        publish(client,"false",sala)
        time.sleep(1)
        publish(client,"true",sala)
        time.sleep(1)

run()
