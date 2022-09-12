# fw_ttest_JORGE_RAMOS

Instrucciones para ejecutar el proyecto:

- Tener lista la ESP32 para ser programada con Micropython.
- Descargar la carpeta firmware_test.
- Subir los archivos descargados a la memoria de la ESP32. Editor Thonny.
- Descargar y configurar el Software ModBusSlave
- Correr el programa

Los datos son enviados al siguiente broker: 
- broker.emqx.io 
- https://www.emqx.com/en/mqtt/mqtt-websocket-toolkit
- Credenciales: user="enerbit", password="enerbit"

TOPICS:
- esp/measure/foundry
- esp/measure/pneumatic
- esp/measure/molding
- esp/measure/warehouse
- esp/measure/pac
- esp/measure/alert

Configuracion del sofware: 
## Setup -> Slave definition
![image](https://user-images.githubusercontent.com/87903340/189740189-ee51c188-1b0b-492b-af05-8f875809ec3e.png)

## Connection -> connect
![image](https://user-images.githubusercontent.com/87903340/189740329-dc4eb81c-0e2f-4eac-a3aa-7d592ec1a990.png)

Se realiza una simulación del PAC3200 por medio de MODBUS/TCP con el sofware mencionado anteriormente. Para que funcione en su red local, debe cambiar la IP Address en el main.py y en la configuración de conexión del software.

![image](https://user-images.githubusercontent.com/87903340/189741353-fe2bb185-7b99-4b5c-94cc-fb9fe33b1860.png)

Se pueden cambiar los valores y se verán reflejados en el dashboard donde se reciben los mensajes MQTT.


El MQTTClient de la ESP32 está suscrito al topic "pc", no realiza ninguna función si se le envía un mensaje, pero sí lo imprime por el terminal.

FORMATO DE ENVÍO DE DATOS:
- Formato de telemetría:
  {
        'procces area': str,
        'fecha': str,
        'hora': str,
        'voltaje L1-N': int,
        'voltaje L2-N': int,
        'voltaje L3-N': int,
        'current L1': int,
        'current L2': int,
        'current L3': int,
        'cumulative Energy imported' : int,
        'power Factor L1': int,
        'power Factor L2': int,
        'power Factor L3': int
  }
  
- Formato de eventos(esp/measure/alert):
  {
      'fecha': str,
      'hora': str,
      'msg': 'Error, overload in any of the variables',
      'procces area': str,
      'payload': alert_dict
  }
  
  alert_dict = {
  '{measure}': int,
  '{measure} recommended': int
  }



## DIAGRAMA DE CONEXIÓN MODBUS ESP32-SIEMENS PAC3200 adjunto.
