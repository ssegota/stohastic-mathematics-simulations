# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:41:31 2017

@author: Student
"""

#Organizirate igu na sreću kod koje se može izgubiti 100 kn s vjerojatnosću od
#60%, dobiti 150 kn s vjerojatnošću od 30% i dobiti 300 kn s vjerojatnošću od 
#10% simulirati igru za 1000 igrača i utvrditi je li igra isplativa
#simulirati 100 ciklusa igre i prikazati zarade stupčastim grafikonom
import numpy as np
import matplotlib.pyplot as plt

#X~ (100   100   150)
#   (0.6 0.3 0.1)
#   (0.6 0.9 1)

def GenerirajX(X):
    S=np.cumsum(X[1])           #formiraj niz kumulativnih suma iz zadanih vjerojatnosti (0.6,0.3,0.1)->(0.6,0.9,0.1)
    i=0                         #iterator u petlji
    ulaz_u_petlju=1             #flag
    u=np.random.rand()          #generiraj u
    while ulaz_u_petlju:
        if u<=S[i]:             #ako nađemo odgovarajuću kumulativnu sumu vjerojatnosti
            broj=X[0][i]        #u broj upišemo stvarnu vrijednost u prvom redu matrice (0) i trenutnog polja i-> drugi redak
            ulaz_u_petlju=0     #postavimo flag za ulaz na ne
        else:
            i=i+1               #ako ne nađemo idemo dalje po polju kumulativnih suma
    return broj

suma = 0

broj_igri=100
dobitci = np.zeros(broj_igri)

for j in range(broj_igri):
    suma = 0
    for i in range(1000):
        suma += GenerirajX([[-100,100,150],[0.6,0.3,0.1]])
    dobitci[j] = suma

plt.bar(range(broj_igri), dobitci)
plt.show()