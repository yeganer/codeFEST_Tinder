from random import random,gauss

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
            return
        self.brake=data['brlt'];
        self.speed=data['speed_GPS'] or data['speed'] or 0
        self.gspeed=data['speed_GPS'];
        self.belt=data['belt'] or 0;
        self.stwa=data['stwa'] or 0;
        self.force=self.speed**2 * self.stwa
        self.ftgs=data['ftgs'];
        #print self.ftgs
        self.speed_lim=data['speed_lim'] or 250;
        #print self.speed, data['speed_GPS'], data['speed']
        self.vehicle_dist=gauss(self.speed/2+10,15);
        self.time = data['time']
