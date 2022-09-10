from random import randint
from ntp_server import LocalTime


class Measure:


    def __init__(self):
        self._foundry = {}
        self._molding = {}
        self._pneumatic = {}
        self._warehouse = {}
        #---callback alert---
        self.cb_alert = None
        #---limit danger measure--
        self.limit_measure = {
        'voltaje L1-N': 240,
        'voltaje L2-N': 240,
        'voltaje L3-N': 240,
        'current L1': 15,
        'current L2': 15,
        'current L3': 15,
        'cumulative Energy imported' : 2000,
        'power Factor L1': 100,
        'power Factor L2': 100,
        'power Factor L3': 100
        }
        #---Set TimeZone---
        self.local_time = LocalTime()
        self.local_time.setRTCWithLocalTime() #Update the RTC at local time zone

    def set_callback(self, fun):
        self.cb_alert = fun


    def _get_measures(self, area):

        measure = {
        'procces area': area,
        'fecha': self.local_time.fecha,
        'hora': self.local_time.hora,
        'voltaje L1-N': randint(40,300),
        'voltaje L2-N': randint(40,300),
        'voltaje L3-N': randint(40,300),
        'current L1': randint(5,20),
        'current L2': randint(5,20),
        'current L3': randint(5,20),
        'cumulative Energy imported' : randint(100,3000),
        'power Factor L1': randint(50,120),
        'power Factor L2': randint(50,120),
        'power Factor L3': randint(50,120)
        }
        self.validate_measures(measure)
        return measure

    def validate_measures(self,measure):
        error_payload = {}
        for key, value in measure.items():
            if(key !='procces area' and key != 'fecha' and key !='hora'): #No validar esas key, no son mediciones
                if( measure[key] > self.limit_measure[key] ):
                    error_payload.update({key:value, '{} recommended'.format(key):self.limit_measure[key]})

        if(bool(error_payload)):#if error_payload is empty
            payload = {
            'fecha': self.local_time.fecha,
            'hora': self.local_time.hora,
            'msg': 'Error, overload in any of the variables',
            'procces area': measure['procces area'],
            'payload': error_payload
            }
            self.cb_alert(payload)



    @property #Getter _foundry
    def foundry(self):
        self._foundry = self._get_measures('foundry')
        return self._foundry

    @property #Getter
    def molding(self):
        self._molding = self._get_measures('molding')
        return self._molding

    @property #Getter
    def pneumatic(self):
        self._pneumatic = self._get_measures('pneumatic')
        return self._pneumatic

    @property #Getter
    def warehouse(self):
        self._warehouse = self._get_measures('warehouse')
        return self._warehouse
