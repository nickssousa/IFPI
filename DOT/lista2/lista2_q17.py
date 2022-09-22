from random import *

listaW= []
listaV= []
vezes= 0

for i in range(1, 11):
  a= randint(0, 11)
  listaW.append(a)
while True:
  try:
    b = int(input("Digite um valor entre 0 e 10: "))
    
    while b< 0 or b>10:
      b= int(input("O número deve estar entre 0 e 10: "))
   
    for j in range(len(listaW)):
      if listaW[j] == b:
        print(f'Ele aparece na posição {j}')
        vezes+=1
    break

  except:
    print("Digite um valor valido.")

print(f'O número digitado se repete {vezes} vezes.')
