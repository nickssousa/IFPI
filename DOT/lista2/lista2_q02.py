lista= []
negativo= []
soma= 0

for i in range(1, 11):
  a= float(input(f'Digite o {i}° número: '))
  lista.append(a)
  
  if a <0:
    negativo.append(a)
  
  if a> 0:
    soma+= a

  if a == 0:
    pass

print(f'Os números digitados são: {lista}')
print(f'Os números negativos são: {negativo}')
print(f'E a soma dos números positivos é: {soma}')
