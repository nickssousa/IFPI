from random import *
l =list(range(100))
pares=[]
impares=[]
par= 0
impar= 0


for i in range(100):
  a= randint(0,100)
  if a %2 ==0:
    par+= 1
    pares.append(a)
  
  else:
    impar+= 1
    impares.append(a)


  
print(f'a) A quantidade de números pares na lista é {par}')
print(f'b) A lista de de números pares: {pares}')
print(f'c) A quantidade de números impares é: {impar}')
print(f'd) A lista de números impares: {impares}')
