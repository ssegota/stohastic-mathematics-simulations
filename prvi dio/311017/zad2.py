# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:39:45 2017

@author: Student
"""

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

def generirajX(x1,x2,x3,p1,p2,p3):
    u = np.random.rand()
    if u < p1:
        res = x1
    elif u < p1+p2:
        res = x2
    else:
        res = x3
    return res

podaci = np.zeros(1000)
for i in range(len(podaci)):
    podaci[i] = generirajX(1,2,3,0.2,0.5,0.3)

#print(a+"\t"+b)
plt.hist(podaci)
plt.show()