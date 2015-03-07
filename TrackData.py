#!/usr/bin/python

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


