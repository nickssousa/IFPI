from random import *
lista1= []
lista2= []

for i in range(10):
  a= randint(-100, 100)
  lista1.append(a)

for num in lista1:
  if num< 0:
    lista2.append(0)
  else:
    lista2.append(num)

print("A primeira lista é: ", lista1)
print("A lista alterada fica: ", lista2)
