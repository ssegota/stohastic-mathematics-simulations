# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:26:35 2017

@author: Student
"""

import numpy as np
import math
import matplotlib.pyplot as plt

#algoritam temeljen na centralnom graničnom teoremu
#za niz jedanko distriuiranih slučajnih varijabli (E(Xi)=mi; V(x)=sigma^2)
#tada njihova suma ima normalnu dirtribuciju sum(xi)~N(n*mi; n*sigma^2)

u = np.zeros(100)
podaci = np.zeros(100)
suma = 0
n = 100
mi = 4
sigma = 3

for j in range(100):
    #zbrojimo iz realizacija
    for i in range(n):
        u[i] = np.random.rand()
        suma += u[i]
    #t formiramo na način:    
    z = (suma-n/2)/math.sqrt(n/12.0)
    #n/2 - oekivanje razdiobe u, 
    #suma-n/2/sqrt(n/12) -> standardizacija ((sum-E(u)/V(u))  -> ~N(0,1)
    suma = 0
    podaci[j] = mi + sigma*z #očekivanju mi dodajemo vrijednost sigma i "pomičemo" tu vrijednost

plt.hist(podaci)
plt.show()