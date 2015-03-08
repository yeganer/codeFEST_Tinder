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


with open("../out/score.dat", "w") as f:
    for k,v in data.items():
        for track in v:
            total=track['score']['total']
            force=track['score']['force']
            sleep=track['score']['sleep']
            limit=track['score']['limit']
            distance=track['score']['distance']
            id = k;
            f.write(str(total) + '\t' + str(sleep) + '\t' + str(force) + '\t' + str(limit) + '\t' + str(distance )+ '\n')
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
