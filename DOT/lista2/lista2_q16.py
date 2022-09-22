from random import *
listaX= []
listaY= []

for i in range(10):
  a= randint(0, 100)
  listaX.append(a)

for num in listaX:
  if num %2 ==0:
    listaY.append(num/2)
  if num%2!= 0:
    listaY.append(num*3)
  
print(listaX)
print(listaY)
