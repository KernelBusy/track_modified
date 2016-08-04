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
from pylab import *
# Get an event
f = open("velojson/1.json")
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
    

num_hits=[]
even = []
for l in range(len(even_det)):
    for i in range(len(even_det[l])):
        even.append(even_det[l][i])
        num_hits.append(part[l][-2])
x_even = []
z_even = []
id_even = [] 

colors = []
i = 0
list_colors = ["b","g","r","m","k","y","c"]
for cont in num_hits:
    for k in range(cont):
        colors.append(list_colors[i])
    if i<(len(list_colors)-1):
        i = i + 1
    else:
        i = 0

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
    plt.plot(r[k],color = colors[k])
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')

dim = np.zeros(len(r[:][0]))
#th_range,u =np.meshgrid(th,dim)

th_range = np.asarray([th]*len(x_even))
x_data = r.flatten()
y_data = th_range.flatten()
n_bins = 10
hist,xedges,yedges = np.histogram2d(x_data,y_data,bins=n_bins)
z_data = hist.flatten()

elements = (len(xedges)-1)*(len(yedges)-1) #Number of boxes
u,v = np.meshgrid(xedges[:-1]+0.25*(xedges[1]-xedges[0]),yedges[:-1]+0.25*(yedges[1]-yedges[0]))
u = u.flatten() # x-coordinate of the bars
v = v.flatten() #y-coordinate of the bars
zpos = np.zeros(elements) #zero-array
dx = 0.5*(u[1]-u[0])*np.ones_like(zpos) # length of the bars along the x-axis
dy = 0.5*(v[n_bins]-v[0])*np.ones_like(zpos)              # length of the bars along the y-axis
dz = hist.flatten()         # height of the bars

ax.bar3d(u, v, zpos,      # lower corner coordinates
         dx, dy, dz)            # width, depth and height
         


plt.show()

"""Another histogram without outliers"""

tol = 4000
dz2 = dz*np.uint8(dz<tol)
hist_outliers = dz2.reshape(shape(hist))

fig2 = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.bar3d(u,v,zpos,dx,dy,dz2) 
plt.show()

"""Color-map"""
# Colormap with outliers

figure()
title("Colormap of r, theta")
imshow(hist)
figure()
title("Colormap of r, theta without the outliers")
imshow(hist_outliers)