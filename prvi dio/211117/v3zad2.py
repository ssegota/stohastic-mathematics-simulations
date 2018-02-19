# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:27:30 2017

@author: Student
"""

#Trajanje nekog projekta noramlno j edistribuirano sa očekivanjem od 7 dana
#i devijavijom od 1 dan.
#a) simulirajte 100 takvih projekata
#b) odredite prosječno trajanje projekta u tih 100 simulacija

import numpy as np
import math
import matplotlib.pyplot as plt

u = np.zeros(100)
podaci = np.zeros(100)
suma = 0
n = 15
mi = 7
sigma = 1
suma2=0
for j in range(100):
    
    for i in range(n):
        u[i] = np.random.rand()
        suma += u[i]
        
    z = (suma-n/2)/math.sqrt(n/12.0)
    
    suma = 0
    podaci[j] = mi + sigma*z 
    
print(np.mean(podaci))

plt.bar(range(100), podaci)
plt.show() 