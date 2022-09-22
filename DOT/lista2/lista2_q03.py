from random import *

lista = []

while True:
  try:
    a= int(input("Digite a quantidade de números que você quer na sua lista: "))
    while a<0:
      a= int(input("O valor não pode ser negativo: "))
    
    for i in range(a):
      lista.append(randint(-20, 20))
    break

  except:
    print("Valor inválido.")

print("A lista na ordem normal: ", lista)
print("A lista na ordem inversa: ", lista[::-1])
