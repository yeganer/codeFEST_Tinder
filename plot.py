#!/usr/bin/python
from mysql import DBLink

list_ID = [101,102,103,104,105,106,107,108]

conf = {
        'ip': '138.246.40.44',
        'user': 'hack',
        'pw': 'Y7ABu',
        'db': 'codefest',
        }
query = "SELECT speed, speed_GPS, stwa from hackathon WHERE Track_VehicleID='{id}'"# LIMIT {limit};"

db = DBLink(conf)

with open(str.format("../out/data_{}.dat", 100), "w") as f:
    for id in list_ID:
        db.query(query.format(id=id))
        for x in db.fetch():
            if (x['speed_GPS'] is not None or x['speed'] is not None) and x['stwa'] is not None:
                speed = x['speed_GPS'] or x['speed'] or 0;
                stwa = x['stwa'] or 0;
            f.write(str(speed) + '\t' + str(stwa) + '\n')
        f.write('\n\n\n')

