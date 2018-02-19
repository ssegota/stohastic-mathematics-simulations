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
    M=[[1,2,3,4],P[int(S-1)]]
    return GenerirajX(M)

#generiraj niz
def GenerirajNiz(S,P,n):
    Niz=np.zeros(n)
    Niz[0]=S
    for i in range(1, n):
        Niz[i]=IduceStanje(Niz[i-1],P)
    return Niz

    
#matrica vjerojatnosti prijelaza
P=[[0.7, 0.2, 0.1, 0.0], 
   [0.0, 0.6, 0.2, 0.2],
   [0.0, 0.0, 0.5, 0.5], 
   [1.0 ,0.0 ,0.0 ,0.0]]

#trenutno stanje
S=1
#broj ponavljanja
n=100


#for i in range(n):
#    if(N[i]==1):
#        print('I')
#    if(N[i]==2):
#        print('D')
#    if(N[i]==3):
#        print('Z')
#    if(N[i]==4):
#        print('L')

n2=100
podaci=np.zeros(n2)
for j in range(n2): 
    N=GenerirajNiz(S,P,n)      
    goodstates=0
    for i in range(n):
        if(N[i]==2):
            goodstates=goodstates+1
    podaci[j]=goodstates/100
    #print(goodstates/100)

V=np.linalg.matrix_power(P, 100)
print("Average of hundred runs=",np.mean(podaci))  
print("Stationary vector value V[2] equals=",V[0][1])
#plt.hist(podaci)