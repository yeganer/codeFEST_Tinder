#!/usr/bin/python
import json
import numpy as np
import time as t

from random import random,gauss,seed
from random import randint

from ContData import *
from TrackData import TrackData
from mysql import DBLink

seed(1337)

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

    speed_lim_cycle = 10;
    curr_speed_lim_cycle = 1;
    prev_speed_lim = randint(20, 160);
    last_time=None
    max_force=None
    tracks = []
    tracks.append(TrackData())
    for x in db.fetch():
        if curr_speed_lim_cycle == speed_lim_cycle:
            prev_speed_lim = randint(40, 140);
            curr_speed_lim_cycle = 1;
            speed_lim_cycle = randint(2, 10);
        else:
            curr_speed_lim_cycle += 1
        x['speed_lim'] = prev_speed_lim;
        x['time'] = t.mktime(t.strptime(x["Node_Time"],"%Y-%m-%d %H:%M:%S"))
        if randint(1,100) == 23:
            x['ftgs'] = True
        else:
            x['ftgs'] = False
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
                if result['force']['max']>max_force:
                    max_force=result['force']['max']
            tracks.append(TrackData())
        try:
            tracks[-1].add_data_point(ContData(x))
        except InvalidDataException as e:
            if debug:
                print 'InvalidDataException: ', e.value, " Number: ", e.count
        last_time=x['time']
        if len(tracks) >10 and False:
            break

with open("out.json","w") as f:
    json.dump(meta, f)

