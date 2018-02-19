# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:30:09 2017

@author: Student
"""

import numpy as np
import matplotlib.pyplot as plt

def bernoulli(p):
    u = np.random.rand()
    if u<=p:
        broj = 1
    else:
        broj = 0
    return broj;

def binomna(n,p):
    broj = 0
    for i in range(n):
        broj += bernoulli(p)
    return broj

polje = np.zeros(1000)
for i in range(1000):
    polje[i] = binomna(100, 0.3)
    #print(polje[i])
    
plt.hist(polje)
plt.show()