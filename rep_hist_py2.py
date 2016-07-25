# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 01:42:50 2016

@author: Ariadna
"""
import numpy as np
import matplotlib as plt
with open('file_hist.dat','r') as f:
    f = f.split()
    hist = []
    for i in f:
        hist.append(f[i])
    bins = np.linspace(0,27,1)
    plt.plot(bins,hist)
    