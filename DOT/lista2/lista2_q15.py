from random import *

listaD= []
listaE= []

for i in range(10):
  a= randint(0, 50)
  listaD.append(a)

for j in range(10):
  listaE.append(listaD[i])
  i-= 1

print(listaD)
print(listaE)
