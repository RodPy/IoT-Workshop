import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO 


servidor_ip = "192.168.0.27"
puerto=1883
cliente='Publicador_Penguin'


#Topic de dispositivos
topic1 = "casa/luz"

#Funciones 
def on_connect(client, userdata, flags, rc):
 print("Connected with result code " + str(rc))
 print("UserData= " + str(userdata))
 print("flags= " + str(flags))
 print("")
 client.subscribe(topic1)

def on_message(client, userdata, message):
    return(message.topic,str(message.payload.decode("utf-8")))
    print("Mensaje recibido=", str(message.payload.decode("utf-8")))
    # print("Topic=", message.topic)
    # print("Nivel de calidad [0|1|2]=", message.qos)
    # print("Flag de retención=", message.retain)
    print("---------------------------------------------")
    print("")
 

client = mqtt.Client(cliente, userdata="Grupo_1") 
client.on_connect = on_connect 
client.on_message = on_message 
# Connecting to the MQTT broker.
client.connect(servidor_ip, puerto, 60) 
client.loop_forever()

LED_PIN = 20 #BCM
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW) 

if on_message[0]==topic1 and on_message[1]='ON':
    GPIO.output(LED_PIN, GPIO.HIGH) 
    time.sleep(1) 
elif on_message[0]==topic1 and on_message[1]='OFF':   
    GPIO.output(LED_PIN, GPIO.LOW) 
    time.sleep(1)
