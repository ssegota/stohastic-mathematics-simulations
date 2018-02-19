# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:43:47 2017

@author: Student
"""

#U nekom razredu ima 20 učenika. Vjerojatnost da učenik dobije odličnu ocijenu
#je 15%. Simulirajte broj odličnih ocijena u 10 razreda, te rezultate prikažite 
#grafički

#demonstrature 12 do 14 u ponedjeljak u knjižnici

import numpy as np
import matplotlib.pyplot as plt

def bernoulli(p):
    u = np.random.rand()
    if u<=p:
        return 1
    else:
        return 0

def binomna(n,p):
    broj = 0
    for i in range(n):
        broj += bernoulli(p)
    return broj

polje = np.zeros(10)
for i in range(10):
    polje[i] = binomna(20, 0.15)
    
plt.bar(range(10), polje)
plt.show()