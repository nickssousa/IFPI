from random import *
preço= [4, 2.8, 9.8, 6.1, 4.8, 1.3, 5.3, 7.6, 2.9, 7.1, 8.4, 6.9, 4.7, 6, 9.1, 4.2, 7.7, 4, 8.6, 4.1, 4.2, 1.1, 4.5, 1.7, 6.3, 8.2, 9, 5, 4.1, 6, 7.4, 8.1, 2.2, 4.2, 2.2, 3.6, 6.6, 1.8, 7.5, 6.1]
faturamento= []
quantidade= []
soma= 0
abaixo= []


def faturamento_medio(x):
  if x< (soma/20):
    abaixo.append(x)
    
for i in range(0,20):
  a= randint(1, 10)
  quantidade.append(a)

for j in range(0,20):
  fat= preço[j]*quantidade[j]
  faturamento.append(fat)
  soma+= fat
  
for k in range(20):
  if faturamento[k] < (soma/20):
    abaixo.append(round(faturamento[k]))


print(f'O faturamento total é {round(soma)}')
print(f'O faturamento médio é {round(soma/20)}')
print(f'E os seguintes faturamentos foram abaixo da média: {abaixo}')
