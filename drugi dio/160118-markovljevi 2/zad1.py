# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:23:27 2018

@author: Student
"""


import numpy as np
import matplotlib.pyplot as plt

#f-ja za generiranje slučajne varijable
def GenerirajX(X):
    S=np.cumsum(X[1])
    i=0
    ulaz_u_petlju=1
    u=np.random.rand()
    while ulaz_u_petlju:
            if u<=S[i]:
                broj=X[0][i]
                ulaz_u_petlju=0
            else:
                i=i+1
    return broj

#X-trenutno sztanje
#prijelazna matrica
def IduceStanje(S,P):
    #to-do
    M=[[1,2,3,0],P[int(S-1)]]
    return GenerirajX(M)

#generiraj niz
def GenerirajNiz(S,P,n):
    Niz=np.zeros(n)
    Niz[0]=S
    for i in range(1, n):
        Niz[i]=IduceStanje(Niz[i-1],P)
    return Niz

    
#matrica vjerojatnosti prijelaza
P=[[0.5, 0.5, 0.0, 0.0], 
   [0.0, 0.5, 0.5, 0.0],
   [0.0, 0.0, 0.5, 0.5], 
   [0.0 ,0.0 ,0.0 ,1.0]]

#trenutno stanje
S=1
#broj ponavljanja
n=100

N=GenerirajNiz(S,P,n)
plt.hist(N)

n2=1000
data=np.zeros(n2)

for i in range(n2):
    N2=GenerirajNiz(S,P,n)
    j=0
    stepstozero=0
    while(N2[j]!=0):
        stepstozero=stepstozero+1    
        j=j+1
    data[i]=stepstozero

print("Average of 100 runs for time spent in good states=",np.mean(data))