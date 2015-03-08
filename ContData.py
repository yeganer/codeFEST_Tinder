from random import random

class InvalidDataException(Exception):
    count=0
    def __init__(self, value):
        InvalidDataException.count+=1
        self.value = value
    def __str__(self):
        return repr(self.value)
#    @classmethod
#    def count(cls):
#        return cls.count

class ContData:
    def __init__(self,data):#speed,gspeed,stwa,belt)
        if data['speed'] is None and data['speed_GPS'] is None:
            raise InvalidDataException(data)
        self.brake=data['brlt'];
        self.speed=data['speed_GPS'] or data['speed'];
        self.gspeed=data['speed_GPS'];
        self.belt=data['belt'] or 0;
        self.stwa=data['stwa'] or 0;
        self.ftgs=data['ftgs'];
        #print self.ftgs
        self.speed_lim=data['speed_lim'] or 250;
        self.vehicle_dist=data['vehicle_dist'] or 250;
        self.time = data['time']
