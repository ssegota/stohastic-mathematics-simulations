# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:47:06 2018

@author: Student
"""
import numpy as np
import matplotlib.pyplot as plt

#T-vrijeme trajanja u satima
#lmbd intenzitet u jedinici vremena lambda

#na neko računalo stiže e-mail po Poissonovom procesu s intenzitetom 10 poruka po satu. 
#Modelirajte i ispišite trenutke u 5 sati u kojima je stigla elektronička pošta

def simulatePoissonProcess(lmbd,T):
    w=np.zeros(1)
    t=0.
    while t<T:
        u = np.random.rand()
        dw = -1./lmbd*np.log(u)
        t = w[-1]+dw
        w= np.append(w,t)
    return w

def plotPoissonProcess1(w):
    K = np.size(w)-1
    t = np.zeros([2*K+1])
    X = np.zeros([2*K+1])
    for k in range(K):
        t[2*k] = w[k]
        t[2*k+1] = w[k]
        X[2*k] = k
        X[2*k+1] = k+1
    t[2*K] = w[K]
    X[2*K] = K
    
    fig = plt.figure()
    plt.plot(t, X) #color='r', linewidth=2.0) 
    plt.title("Poissonov proces")
    plt.xlabel("t")
    plt.ylabel("N(t)")
    fig.show()

    
W = simulatePoissonProcess(10, 5)
plotPoissonProcess1(W)

print(W)

