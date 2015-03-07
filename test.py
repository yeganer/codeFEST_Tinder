#!/usr/bin/python
import numpy as np
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

class TrackData:
    def __init__(self,data):
        self.f_end=0;
        self.v_max=0;
        self.v_avg=0;
        self.v_var=0;
        self.p_limit=0;
        self.p_distance=0;
        self.p_belt=0;
        self.curves=0;
        self.finish=0;
        self.acc=0;
        self.data=list()
        for i in xrange(len(data)):
            self.add_datapoint(data[i])

    def add_datapoint(self,data):
        self.data.append(data)
        self.update()
        return

    def update(self):
        #mspeed,avg
        #for k,v in self.data.items():
        #speed = 
        avg_speed = np.mean([x.speed for x in self.data])
        print(avg_speed)

    def export(self, path):
        #'''creates a file with the track data'''
        return



data=[{
        'speed' : 30.,
        'stwa' : 100.,
        'ftgs' : 100.,
        'gspeed' : 100.,
        'avg_speed' : 100.,
        'max_speed' : 100.,
        'time' : 100.,
        'speed_var' : 100.,
        'distance' : 100.,
        'speed_lim' : 100.,
        'belt' : True,
        'crash' : False,
        'brake' : False,
        'sleepines' : False,
        'curve' : False,
        },{
        'speed' : 150.,
        'stwa' : 100.,
        'ftgs' : 100.,
        'gspeed' : 100.,
        'avg_speed' : 100.,
        'max_speed' : 100.,
        'time' : 100.,
        'speed_var' : 100.,
        'distance' : 100.,
        'speed_lim' : 100.,
        'belt' : True,
        'crash' : False,
        'brake' : False,
        'sleepines' : False,
        'curve' : False,
        },{
        'speed' : 100.,
        'stwa' : 100.,
        'ftgs' : 100.,
        'gspeed' : 100.,
        'avg_speed' : 100.,
        'max_speed' : 100.,
        'time' : 100.,
        'speed_var' : 100.,
        'distance' : 100.,
        'speed_lim' : 100.,
        'belt' : True,
        'crash' : False,
        'brake' : False,
        'sleepines' : False,
        'curve' : False,
        }]

a=list()
for i in xrange(len(data)):
    a.append(ContData(data[i]))
b = TrackData(a)
b.export('')
