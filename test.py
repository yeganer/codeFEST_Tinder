#!/usr/bin/python
import numpy as np
from random import random

from ContData import ContData
from TrackData import TrackData



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

a=list()
for i in xrange(len(data)):
    a.append(ContData(data[i]))
b = TrackData(a)
b.export('')
