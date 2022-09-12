import machine
from umqtt.simple import MQTTClient
from wifi_connection import wifi_connect
from measures import Measure
import json
from time import sleep, time

from umodbus.uModBusTCP import uModBusTCP

try:
    #---Connection WIFI----
    wifi_connect("Nada_Es_Gratis","Angelyjorge")

    #---Config MQTT protocol----
    def received_msg(topic, msg):
        print('topic: {} - msg {}'.format(topic,msg))

    client = MQTTClient("ESP32","broker.emqx.io", 1883, user="enerbit", password="enerbit")
    client.connect()
    client.set_callback(received_msg)
    client.publish('esp', 'Hola desde ESP32')
    client.subscribe('pc')

    #---Measures SIEMENS PAC3200----
    def alert_event(payload):
        print('Alert Event is up')
        #print(payload)
        client.publish('esp/measure/alert', json.dumps(payload))

    measure = Measure(slave_ip = '192.168.100.13')#Config MODBUS/TCP tambien
    measure.set_callback(alert_event)
    
    #measure44 = Measure(slave_ip = '192.168.100.44')#Config MODBUS/TCP 
    #measure44.set_callback(alert_event)
    
except Exception as e:
    print('Ha ocurrido un error! Reintentando...', e)
    sleep(2)
    machine.reset()#Resetea la ESP32 cuando hay un error en las conexiones anteriores


#print('Conectado, MODBUS:', host)
#---LOOP---
anterior = time()
while True:
    client.check_msg()#Chequear si llegó un mensaje a los topicos subscritos
    if(time() - anterior == 5): #Cada 5 segs
        anterior = time()
        client.publish('esp/measure/foundry', json.dumps(measure.foundry))#Simulados randint()
        client.publish('esp/measure/molding', json.dumps(measure.molding))
        client.publish('esp/measure/pneumatic', json.dumps(measure.pneumatic))
        client.publish('esp/measure/warehouse', json.dumps(measure.warehouse))
        client.publish('esp/measure/pac', json.dumps(measure.pac))#Simulacion PAC3200 - mbsSlave.exe






