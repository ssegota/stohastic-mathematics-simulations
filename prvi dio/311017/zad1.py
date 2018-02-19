# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:27:10 2017

@author: Student
"""

import numpy as np
import matplotlib.pyplot as plt

#X~ (1   2   3)
#   (0.2 0.5 0.3)
#   (0.2 0.7 1)



podaci = np.zeros(1000)
for i in range(len(podaci)):
    a = np.random.rand()
    if (a < 0.2):
        podaci[i] = 1
    elif (a < 0.7):
        podaci[i] = 2
    else:
        podaci[i] = 3

#print(a+"\t"+b)
plt.hist(podaci)
plt.show()