# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:27:41 2017

@author: Student
"""
#box-muller

import numpy as np
import math
import matplotlib.pyplot as plt
podaci = np.zeros(100)
mi = 4
sigma = 3

for i in range(100):
    u1 = np.random.rand()
    u2 = np.random.rand()
    z = math.sqrt(-2*math.log(u1))*math.sin(2*math.pi*u2)
    podaci[i] = mi + sigma*z

plt.hist(podaci)
plt.show()

print(np.mean(podaci))