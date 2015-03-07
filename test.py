#!/usr/bin/python
import numpy as np
from random import random

from ContData import ContData
from TrackData import TrackData
from mysql import DBLink

import time as t


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
#
#a=list()
#for i in xrange(len(data)):
#    a.append(ContData(data[i]))
#b = TrackData(a)
#print b.export('')

conf = {
        'ip': '138.246.40.44',
        'user': 'hack',
        'pw': 'Y7ABu',
        'db': 'codefest',
        }

db = DBLink(conf)
query = "SELECT speed, speed_GPS, brlt, belt, stwa, ftgs, Node_Time from hackathon WHERE Track_VehicleID='{id}' ORDER BY NODE_TIME"# LIMIT {limit};"
db.query(query.format(id=101, limit=10))
last_time=None
tracks = []
tracks.append(TrackData())
for x in db.fetch():
    x['speed_lim']=200;
    x['vehicle_dist']=200;
    x['time'] = t.mktime(t.strptime(x["Node_Time"],"%Y-%m-%d %H:%M:%S"))
    #print time
    if not last_time:
        last_time=x['time']
    if np.abs(x['time']-last_time) > 1800:
        tracks[-1].update()
        print tracks[-1].export('')
        tracks.append(TrackData())
    tracks[-1].add_data_point(ContData(x))
    last_time=x['time']
    if len(tracks) >100:
        break
