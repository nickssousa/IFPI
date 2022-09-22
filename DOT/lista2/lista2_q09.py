from random import *

listaX = []
listaY= []
    
for i in range(5):
  listaX.append(randint(-10, 10))

for i in range(4, -1, -1):
  listaY.append(listaX[i])


print(listaX)
print(listaY)
