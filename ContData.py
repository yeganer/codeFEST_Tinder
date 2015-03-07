from random import random

class ContData:

    def __init__(self,data):#speed,gspeed,stwa,belt)
        self.brake=data['brlt'];
        self.speed=data['speed'];
        self.gspeed=data['speed_GPS'];
        self.belt=data['belt'];
        self.stwa=data['stwa'];
        self.ftgs=data['ftgs'];
        self.speed_lim=data['speed_lim'];
        self.vehicle_dist=data['vehicle_dist'];
        self.time = data['time']
