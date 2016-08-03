# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 21:38:18 2016

@author: Ariadna
"""

import event_model as em
import validator_lite as vl
import json
import matplotlib.pyplot as plt   
from validator_lite import *
import numpy as np


# Get an event
f = open("velojson/2.json")
json_data = json.loads(f.read())
event = em.event(json_data)
f.close()

tracks = event.montecarlo
part = tracks["particles"]
histo = []
hits_id = event.event["hit_id"]
n_tracks = len(part)
index = event.event["sensor_hits_starting_index"]
sensors = event.number_of_sensors
even_det = []
for j in range(0,sensors-1,2):
    even_det.append(hits_id[index[j]:index[j+1]])

even = []
for l in range(len(even_det)):
    for i in range(len(even_det[l])):
        even.append(even_det[l][i])

for i in range(n_tracks): 
    if all(x in even for x in part[i][-1]):
        histo.append(part[i][-2])
plt.hist(histo,bins = 25)
plt.title("Track's length in the even detectors")
plt.xlabel("Length of the track")
plt.ylabel("# of tracks")
plt.show()