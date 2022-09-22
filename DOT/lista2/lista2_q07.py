from random import *
lista= []


for i in range(10):
  a= randint(-10,10)
  lista.append(a)


while True:
  try:
    b= int(input("Digite um número: "))
    if b in lista:
      print("O valor está na lista!")
      print(lista)

    else:
      print("O valor não está na lista")
      print(lista)

    break

  except:
    print("Valor inválido.")
