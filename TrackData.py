#!/usr/bin/python

import numpy as np

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
        self.score=0;
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
        l_speed = [x.speed for x in self.data]
        self.v_avg = np.mean(l_speed)
        self.v_max = np.max(l_speed)
        self.v_var = np.var(l_speed)
        self.acc = [np.abs(l_speed[i] - l_speed[i+1]) for i in xrange(len(l_speed)-1)]
        self.p_limit = np.mean([1 if x.speed>x.speed_lim else 0 for x in self.data])
        self.p_belt = np.mean([1 if x.belt else 0 for x in self.data])
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
                'belt':self.p_belt,}


