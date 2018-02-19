# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:27:46 2017

@author: Student
"""

#algoritam prihvačanja i odbacivanja
# 2 razdiobe 1 znamu generirati, a jednu ne
#ova koju znamo majorizira nepoznatu
# npr generiramo uniformnu za aproksimaciju beta razdiobe
#generiramo slučajnu vrijednost

#PRIMJER
#f(x) = 60x♠^3(1-x)^2
import numpy as np
import matplotlib.pyplot as plt

def fbeta(x):
    #fbeta= lambda x:60*x*3(1-x)**2
    fbeta = 60*x**3*(1-x)**2
    return fbeta


podaci = np.zeros(100)

for i in range(100):
    flag = True
    while flag:
        p = np.random.rand() #x-os
        u = np.random.rand() #učestalost
        if 3*u<fbeta(p): #3*u - normalizacija i majorizacija sl. var. u
            x=p
            flag=False
    podaci[i] = x
    
plt.hist(podaci)
plt.show()