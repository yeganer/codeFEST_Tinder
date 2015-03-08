#!/usr/bin/python
import json
import numpy as np
import time as t

from random import random

from ContData import *
from TrackData import TrackData
from mysql import DBLink


debug=False

list_ID = [101,102,103,104,105,106,107,108]

conf = {
        'ip': '138.246.40.44',
        'user': 'hack',
        'pw': 'Y7ABu',
        'db': 'codefest',
        }
query = "SELECT speed, speed_GPS, brlt, belt, stwa, ftgs, Node_Time from hackathon WHERE Track_VehicleID='{id}' ORDER BY NODE_TIME"# LIMIT {limit};"

db = DBLink(conf)
meta = {}
for i in list_ID:
    db.query(query.format(id=i, limit=10))
    meta[i] = []

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
        if np.abs(x['time']-last_time) > 1800 and len(tracks[-1].data)>1:
            tracks[-1].end_track()
            result = tracks[-1].export()
            if result:
                meta[i].append(result)
                if not max_force:
                    max_force =0
                if result['force'][2]>max_force:
                    #print(len(tracks))
                    max_force=result['force'][2]
                #print result['max_force'], ' ', result['avg_force'], ' ', result['var_force']
                #print result['score']
            #print len(tracks)
            tracks.append(TrackData())
        try:
            tracks[-1].add_data_point(ContData(x))
        except InvalidDataException as e:
            if debug:
                print 'InvalidDataException: ', e.value, " Number: ", e.count
        last_time=x['time']
        if len(tracks) >1 and True:
            break
    #print max_force


with open("out.json","w") as f:
    json.dump(meta, f)

