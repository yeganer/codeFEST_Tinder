#!/usr/bin/python
import numpy as np
from random import random

from ContData import *
from TrackData import TrackData
from mysql import DBLink

import time as t


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
max_force=None
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
        tracks[-1].end_track()
        result = tracks[-1].export()
        if result:
            if not max_force:
                max_force =0
            if result['force']>max_force:
                print(len(tracks))
                max_force=result['force']
            #print result
        #print len(tracks)
        tracks.append(TrackData())
    try:
        tracks[-1].add_data_point(ContData(x))
    except InvalidDataException as e:
        print 'InvalidDataException: ', e.value, " Number: ", e.count
    last_time=x['time']
    if len(tracks) >26 and False:
        break
#print max_force
