#!/usr/bin/python
from mysql import DBLink
import json
import time

list_ID = [101,102,103,104,105,106,107,108]

conf = {
        'ip': '138.246.40.44',
        'user': 'hack',
        'pw': 'Y7ABu',
        'db': 'codefest',
        }
db = DBLink(conf)

json_data = open("out.json")
data = json.load(json_data)


for k,v in data.items():
    for track in v:
        start = track["time"]["start"];
        end = track["time"]["end"];
        id = k;
        print start, end, id
        q_start = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
        q_end = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end))

        query = "SELECT speed, speed_GPS, stwa from hackathon where Node_Time > '{start}' AND Node_Time < '{end}' AND Track_VehicleID = '{id}'";
        db.query(query.format(start=q_start, end=q_end, id=id))
        with open(str.format("../out/data_{}_{}.dat", id, start), "w") as f:
            for x in db.fetch():
                if (x['speed_GPS'] is not None or x['speed'] is not None) and x['stwa'] is not None:
                    speed = x['speed_GPS'] or x['speed'] or 0;
                    stwa = x['stwa'] or 0;
                    print speed, stwa
                f.write(str(speed) + '\t' + str(stwa) + '\n')
            f.write('\n\n\n')
                

'''
query = "SELECT speed, speed_GPS, stwa from hackathon WHERE Track_VehicleID='{id}'"# LIMIT {limit};"
with open(str.format("../out/data_{}.dat", 100), "w") as f:
    for id in list_ID:
        db.query(query.format(id=id))
        for x in db.fetch():
            if (x['speed_GPS'] is not None or x['speed'] is not None) and x['stwa'] is not None:
                speed = x['speed_GPS'] or x['speed'] or 0;
                stwa = x['stwa'] or 0;
            f.write(str(speed) + '\t' + str(stwa) + '\n')
        f.write('\n\n\n')
'''
