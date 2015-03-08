#!/usr/bin/python

import numpy as np
import math

class TrackData:
    def __init__(self,data=None):
        #self.v_max=0;
        #self.v_avg=0;
        #self.v_var=0;
        #self.p_limit=0;
        #self.p_distance=0;
        #self.p_belt=0;
        #self.curves=0;
        #self.acc=0;
        #self.score=0;
        #self.duration=0
        self.finish=False;
        self.data=list()
        self.error=False
        if data:
            for i in xrange(len(data)):
                self.add_datapoint(data[i])

    def end_track(self):
        self.update()
        self.finish=True;

    def add_data_point(self,data):
        if self.finish:
            return False
        if not data.stwa:
            data.stwa=0
        if data.speed:
            self.data.append(data)
        #self.update()
        return

    def update(self):
        if len(self.data)>2:
            self.score={}
            lspeed = [x.speed for x in self.data]
            self.v = {
                    'avg' : np.mean(lspeed),
                    'std' : np.std(lspeed),
                    'max' : np.max(lspeed),
                    }
            self.acc = np.mean([np.abs(lspeed[i] - lspeed[i+1]) for i in xrange(len(lspeed)-1)])

            self.score['limit'] = 1-np.mean([1 if x.speed>x.speed_lim else 0 for x in self.data])
            self.score['sleep'] = 1-np.mean([1 if x.ftgs else 0 for x in self.data])
            self.score['distance'] = np.mean([1 if x.vehicle_dist>x.speed/2. else 0 for x in self.data])

            times = [x.time for x in self.data]
            self.duration=np.max(times) - np.min(times)

            self.max_angle=np.max([np.abs(x.stwa) for x in self.data])

            l_force = [np.abs(x.force) for x in self.data]
            self.score['force'] = math.exp(-len([1 for x in self.data if np.abs(x.force) > 300000 ])/5.)
            #self.p_force = [x]
#            self.max_force=np.max(l_force)
#            self.force_avg=np.mean(l_force)
#            self.force_var=np.std(l_force)
            self.force={
                    'max':np.max(l_force),
                    'avg':np.mean(l_force),
                    'med':np.median(l_force),
                    'std':np.std(l_force),
                    #'max':np.max(l_force),
                    #'max':np.max(l_force),
                    }
            #print self.force
            #test = [(np.abs(x.stwa),x.speed) for x in self.data if x.speed>80 and x.stwa >40]
            #print(avg_speed=)
            l_tmp_belt = [[int(digit) for digit in bin(int(x.belt))[2:]] for x in self.data if x.belt is not None]
            l_belt = [[0]*(18-len(tmp_belt))+tmp_belt for tmp_belt in l_tmp_belt]
            if l_belt:
                l_driver_belt = [belt[-2] for belt in l_belt]
                seats = max([len([x for x in belt[1::2] if x%2]) for belt in l_belt])
                belted = [len([t for t in zip(belt,belt[1:])[0::2] if t[0] and t[1]]) for belt in l_belt]
                self.p_belt = np.mean(l_driver_belt)
            else:
                self.p_belt = -1
            self.calc_total_score()
        else:
            self.error=True

    def calc_total_score(self):
        self.score['total'] = np.average(
                (
                    self.score['force'],
                    self.score['limit'],
                    self.score['distance'],
                    self.score['sleep'],
                    ),
                weights=(1,1,1,1)
                )
        print 'total: ', self.score['total']

    def export(self):
        if not self.error:
            return {'v': self.v,
                    'acc':self.acc,
                    'score':self.score,
                    'duration':self.duration,
                    'angle':self.max_angle,
                    'force':self.force,
                    'belt':self.p_belt,}
        else:
            return None


