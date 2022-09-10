import network
import time

def wifi_connect(ssid, psw):
    sta_if = network.WLAN(network.STA_IF)
    #sta_if.disconnect()
    sta_if.active(True)
    sta_if.connect(ssid, psw)
    i=0
    while not sta_if.isconnected():
       print("Conectando... {}".format(i))
       i=i+1
       time.sleep_ms(100)
       if(i>100):
           raise

    print("Conexion WIFI completada.")
