import Adafruit_DHT
import time 
sensor = Adafruit_DHT.DHT11
pin =21
3## TEMP mayor a 25 ROJO, MENOR A 25 AMARILLO y MAYOR A 20, 
# MENOR A 20 VERDE
while True:
    lectura =Adafruit_DHT.read_retry(sensor,pin)
    humedad=lectura[0]
    temperatura=lectura[1]

    print("La Humedad es: "+ str(humedad) + ". La Temp es: " + str(temperatura) )
    time.sleep(5)