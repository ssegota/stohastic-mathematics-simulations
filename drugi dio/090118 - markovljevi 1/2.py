# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:31:28 2018

@author: Student
"""

#formirati 10 iducih stanja prema zadatku 1

import numpy as np

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
    M=[[1,2],P[int(S-1)]]
    return GenerirajX(M)

#generiraj niz
def GenerirajNiz(S,P,n):
    Niz=np.zeros(n)
    TrenutnoStanjeUNizu=S
    for i in range(n):
        Niz[i]=TrenutnoStanjeUNizu
        TrenutnoStanjeUNizu=IduceStanje(S,P)
    return Niz

    
#matrica vjerojatnosti prijelaza
P=[[0.9,0.1], [0.2,0.8]]
#trenutno stanje
S=1
n=10

N=GenerirajNiz(S,P,n)
print(N)