from machine import RTC
import ntptime



class LocalTime:

    def __init__(self):
        self._fecha = ''
        self._hora = ''
        self.rtc = RTC()

    def setRTCWithLocalTime(self):
        ntptime.settime()# set el rtc datetime del ESP32 desde el servidor remoto de NTP. La hora que obtiene de NTP es UTC + 0 
        year, month, day, weekday, hour, minute, seconds, m_seconds = list(self.rtc.datetime())
        self.rtc.init((year, month, day, weekday, (hour -5), minute, seconds, m_seconds))#Colombia es UTC-5, por eso se restan 5 horas


    @property
    def fecha(self):
        list_RTC = list(self.rtc.datetime())
        self._fecha = '{}/{}/{}'.format(list_RTC[2], list_RTC[1], list_RTC[0])
        return self._fecha

    @property
    def hora(self):
        list_RTC = list(self.rtc.datetime())
        self._hora = '{}:{}:{}'.format(list_RTC[4], list_RTC[5], list_RTC[6])
        return self._hora
