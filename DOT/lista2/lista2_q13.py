from random import *
k =0
l= 0
m= 0
n= 0
o= 0
p= 0

    
a= int(input("Digite o número de vezes que se deseja jogar um dado: "))
while a<1:
  a= int(input("O número digitado deve ser positivo: "))
for i in range(a):
  z = randint(1,7)
  if z == 1:
    k+= 1
  
  if z == 2:
    l+= 1

  if z == 3:
    m+= 1

  if z == 4:
    n+= 1

  if z == 5:
    o+= 1

  if z == 6:
    p+= 1


print(f'O lado 1 caiu {k} vezes, o lado 2 caiu {l} vezes,  o lado 3 caiu {m} vezes,  o lado 4 caiu {n} vezes,  o lado 5 caiu {o} vezes,  o lado 2 caiu {p} vezes.')
