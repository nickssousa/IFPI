mes= ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temp= []
soma= 0

for i in range(12):
    a= float(input())
    b= input().upper().strip()

    if b == 'C':
        a+= 273.15
        soma+= a

    if b == 'F':
        a= (a+ 459.67)*5/9
        soma+= a

    if b == 'K':
        soma+= a

    temp.append(a)

media= soma/12

print('TEMPERATURA MÉDIA ANUAL')
print(f'{round(media, 2)}K')
print('TEMPERATURAS ACIMA DA MÉDIA ANUAL:')
for j in range(12):
    if temp[j] > media:
        print(f'{mes[j]}: {round(temp[j], 2)}K')
