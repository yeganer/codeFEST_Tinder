from random import random

class ContData:

    def __init__(self,data):#speed,gspeed,stwa,belt)
        self.speed=data['speed'];
        self.gspeed=data['gspeed'];
        self.brake=data['brake'];
        self.stwa=data['stwa'];
        self.ftgs=data['ftgs'];
        self.speed_lim=data['speed_lim'];
        self.vehicle_dist=['vehicle_dist'];
        
