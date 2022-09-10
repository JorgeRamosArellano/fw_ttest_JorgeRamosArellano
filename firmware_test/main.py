import machine
from umqtt.simple import MQTTClient
from wifi_connection import wifi_connect
from measures import Measure
import json
from time import sleep, time

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
        print(payload)
        client.publish('esp/measure/alert', json.dumps(payload))

    measure = Measure()
    measure.set_callback(alert_event)
except:
    print('Ha ocurrido un error! Reintentando...')
    sleep(2)
    machine.reset()

#---LOOP---
anterior = time()
while True:
    client.check_msg()
    if(time() - anterior == 5):
        anterior = time()
        client.publish('esp/measure/foundry', json.dumps(measure.foundry))
        client.publish('esp/measure/molding', json.dumps(measure.molding))
        client.publish('esp/measure/pneumatic', json.dumps(measure.pneumatic))
        client.publish('esp/measure/warehouse', json.dumps(measure.warehouse))







