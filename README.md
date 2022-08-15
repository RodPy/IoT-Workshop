# IoT-Workshop

Paquetes pip necesarios 
pip install paho-mqtt
pip install Adafruit-DHT

Programas necesarios 
sudo apt-get install mosquitto mosquitto-clients

Configuracion de mosquitto
sudo echo 'listener 1883' >> /etc/mosquitto/mosquitto.conf
sudo echo 'allow_anonymous true' >> /etc/mosquitto/mosquitto.conf