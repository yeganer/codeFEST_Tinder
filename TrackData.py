#!/usr/bin/python

import numpy as np
import math

class TrackData:
    def __init__(self,data=None):
        self.v_max=0;
        self.v_avg=0;
        self.v_var=0;
        self.p_limit=0;
        self.p_distance=0;
        self.p_belt=0;
        self.curves=0;
        self.finish=False;
        self.acc=0;
        self.score=0;
        self.data=list()
        self.duration=0
        if data:
            for i in xrange(len(data)):
                self.add_datapoint(data[i])

    def end_track(self):
        self.finish=True;

    def add_data_point(self,data):
        if self.finish:
            return False
        if data.speed:
            self.data.append(data)
        #self.update()
        return

    def update(self):
        if len(self.data)>2:
            #mspeed,avg
            #for k,v in self.data.items():
            #speed = 
            l_speed = [x.speed for x in self.data]
            self.v_avg = np.mean(l_speed)
            self.v_max = np.max(l_speed)
            self.v_var = np.std(l_speed)
            self.acc = np.mean([np.abs(l_speed[i] - l_speed[i+1]) for i in xrange(len(l_speed)-1)])
            self.p_limit = 1-np.mean([1 if x.speed>x.speed_lim else 0 for x in self.data])
            self.p_belt = np.mean([1 if x.belt else 0 for x in self.data])
            self.p_sleep = 1-np.mean([1 if x.ftgs else 0 for x in self.data])
            self.p_distance = np.mean([1 if x.vehicle_dist>x.speed/2. else 0 for x in self.data])
            self.score=np.mean([self.p_limit, self.p_belt, self.p_distance])
            self.score=np.mean([self.score, math.exp(-self.v_var)])
            times = [x.time for x in self.data]
            self.duration=np.max(times) - np.min(times)
            #print(avg_speed)
    
    def export(self, path):
        #'''creates a file with the track data'''
        #print(self.v_avg)
        #print(self.v_max)
        #print(self.v_var)
        #print(self.p_limit)
        return {'v_avg':self.v_avg,
                'v_var':self.v_var,
                'v_max':self.v_max,
                'limit':self.p_limit,
                'acc':self.acc,
                'score':self.score,
                'dist':self.p_distance,
                'duration':self.duration,
                'belt':self.p_belt,}


