from random import random

class ContData:

    def __init__(self,data):#speed,gspeed,stwa,belt)
        self.speed=data['speed'];
        self.gspeed=data['gspeed'];
        self.brake=data['brake'];
        self.stwa=data['stwa'];
        self.ftgs=data['ftgs'];
        self.lspeed=random()*100.+30

    def get_curve(self):
        return self.stwa*1./self.speed


