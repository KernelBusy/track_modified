# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:18:42 2016

@author: Ariadna
"""

import event_model as em
import validator_lite as vl
import json
import matplotlib.pyplot as plt   
from validator_lite import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from numpy import histogram2d

# Get an event
f = open("velojson/0.json")
json_data = json.loads(f.read())
event = em.event(json_data)
f.close()

tracks = event.montecarlo
part = tracks["particles"]
hits = []
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

x_even = []
z_even = []
id_even = [] 

for i in range(n_tracks): 
    if all(x in even for x in part[i][-1]):
        id_even.append(part[i][-1])
        for k in part[i][-1]:
            x_even.append(event.event["hit_x"][event.event["hit_id"].index(k)])
            z_even.append(event.event["hit_z"][event.event["hit_id"].index(k)])
            

r = []
th = np.arange(0,np.pi,0.1)
for i in range(len(x_even)):
    for theta in th:
        r.append(abs(x_even[i]*np.cos(theta) + z_even[i]*np.sin(theta)))

r=np.reshape(r,(len(x_even),len(r)/len(x_even)))
for k in range(0,len(x_even)):
    plt.plot(r[k])
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')

dim = np.zeros(381)
th_range,u =np.meshgrid(th,dim)
x_data = r.flatten()
y_data = th_range.flatten()

#elements = (len(x_even)*len(th)-1)*(len(y_even)-1)
#x_data,y_data = np.meshgrid(np.arange(r.shape[1]),np.arange(r.shape[0]))
#x_data = np.array(x_data)
#y_data = np.array(y_data)
#x_data = x_data.flatten()
#y_data = y_data.flatten()
#zpos = np.zeros(elements)
th_range = np.asarray([th]*len(x_even))
hist,xedges,yedges = np.histogram2d(x_data,y_data)
z_data = hist.flatten()
u,v = np.meshgrid(xedges[:-1]+0.25,yedges[:-1]+0.25)
u = u.flatten()
v = v.flatten()
dx = 0.1*np.ones_like(u)
dy = 0.1*np.ones_like(v)
dz = np.ones_like(z_data)

ax.bar3d(u,v,z_data,dx,dy,dz)
plt.show()


"""
xpos,ypos =np.meshgrid(xedges[:-1] + 0.1,yedges[:-1]+0.1)

xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(elements)
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz.hist.flatten()"""


    
    