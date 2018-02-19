# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 11:31:15 2018

@author: Student
"""

#Markovljevi lanci
#############################################################################
#diskretno vrijeme
#slijedeće stanje ovisi SAMO o trenutnom stanju, ne o prošlima
#Markovljeve lance dijelimo na pergodičke i absorbirajuće
#kod pergodičkih mođžemo iz svakog stanja kroz vrijeme preći u bilo koje stanje
#kod absorbirajučih je moguće doći u stanje iz kojega je nemoguće izači

#matrični zapis lanca sa prijelaznim vjerojatnostima
#    1       2
#1   [0,9; 0,1]
#2   [0,2; 0,8]

#početni vektor je [0;1] želimo simulirati slijedeće stanje
#znači da je prijelazna matrica [0,9;0,1] respektivno za prijelaz iz stanja 1 u stanje 1 ili 2

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
    #generiranje matrice
    M=[[1,2],P[int(S-1)]]
    return GenerirajX(M)



    
#matrica vjerojatnosti prijelaza
P=[[0.9,0.1], [0.2,0.8]]
#trenutno stanje
S=1

print(IduceStanje(S,P))


