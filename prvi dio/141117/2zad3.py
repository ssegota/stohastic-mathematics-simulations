# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:51:28 2017

@author: Student
"""
#eksponencijalna
#F(X)=1-e^(lambda*x)
#y=(ln(1-x))/lambda --> inverzna f-ja


#napraviti algoritam koji generira slučajan broj koji je distribuiran po
#erlangovoj razdiobi
#suma od k realizacija eksponencijalne rauzdiobe ima erlangovu razdiobu
import numpy as np
import matplotlib.pyplot as plt
import math

def eksponencijalna(a):
    u = np.random.rand()
    return (-1)*math.log(1-u)/a
    
def erlang(k, a):
    broj = 0;
    for i in range(k):
        broj += eksponencijalna(a)
    return broj
 
polje = np.zeros(1000)
for i in range(1000):
    polje[i] = erlang(100, 2)
    
plt.hist(polje)
plt.show