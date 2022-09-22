from random import *

listaX= []
listaR= []

for i in range(10):
  a= randint(-5, 5)
  listaX.append(a)

for j in range(len(listaX)):
  if listaX[j] < 0:
    listaR.append(listaX[j])
  
print(listaX)
print(listaR)
