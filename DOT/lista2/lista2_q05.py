from random import *
lista1= []
lista2= []

for i in range(10):
  a= randint(0, 100)
  lista1.append(a)
  b= randint(0, 100)
  lista2.append(b)

def intercalar(l1, l2):
  l3 = l1 + l2 
  l3[::2] = l1 
  l3[1::2] = l2
  return l3

print("A primeira lista é: ", lista1)
print("A segunda lista é: ", lista2)
print ("A lista intercalada é: %s" %intercalar(lista1, lista2)) 
