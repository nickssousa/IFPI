from random import *
lista= []
maior= 0
menor= 9999999999999999
posição_maior= 0
posição_menor= 0

for i in range(1, 16):
  a= randint(-100, 100)
  lista.append(a)

  if a> maior:
    maior= a
    posição_maior= i
  
  if a< menor:
    menor= a
    posição_menor= i

print("Os valores são: %s"% lista)
print(f'O maior deles é {maior} e foi o {posição_maior}° valor digitado')
print(f'O menor deles é {menor} e foi o {posição_menor}° valor digitado')
