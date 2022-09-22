from random import *

listaR= []
listaX= []

def juntar(lista1,lista2):
   unido = list(lista1 + lista2)
   return unido


for i in range(5):
  listaR.append(randint(0,10))

for j in range(10):
  listaX.append(randint(-5,5))

print("A lista R é: ", listaR)
print("A lista X é: ", listaX)
print("As duas unidas é: ", juntar(listaR, listaX))
