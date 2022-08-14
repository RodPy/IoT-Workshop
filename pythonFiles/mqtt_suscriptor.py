import paho.mqtt.client as mqtt


servidor_ip = "192.168.0.27"
puerto=1883

#Topic de dispositivos
topic = "casa/habitaciones/hab1/luz"

#Funciones 
def on_connect(client, userdata, flags, rc):
 print("Connected with result code " + str(rc))
 print("UserData= " + str(userdata))
 print("flags= " + str(flags))
 print("")
 client.subscribe(topic)

def on_message(client, userdata, message):
 print("Mensaje recibido=", str(message.payload.decode("utf-8")))
 print("Topic=", message.topic)
 print("Nivel de calidad [0|1|2]=", message.qos)
 print("Flag de retención=", message.retain)
 print("---------------------------------------------")
 print("")

client = mqtt.Client('Cliente1', userdata="UsuarioDePrueba") 
client.on_connect = on_connect 
client.on_message = on_message 
client.connect(servidor_ip, puerto, 60) 
client.loop_forever()