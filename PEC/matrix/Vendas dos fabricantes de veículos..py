ano= ['2013', '2014', '2015', '2016', '2017', '2018']
fiat= []
ford= []
gm= []
wolkswagen= []
carros= ['Fiat', 'Ford', 'GM', 'Wolkswagen']

somat= 0
soma1= 0
soma2= 0 
soma3= 0
soma4= 0
venda= 0
cu= 0
eita= 0

for i in range(6):
    x= int(input())
    fiat.append(x)
    soma1+= x

for i in range(6):
    z= int(input())
    ford.append(z)
    soma2+= z

for i in range(6):
    y= int(input())
    gm.append(y)
    soma3+= y

for i in range(6):
    u= int(input())
    wolkswagen.append(u)
    soma4+= u

for i in range(6):
    somat= fiat[i] + ford[i] + gm[i] + wolkswagen[i]
    if somat> venda:
        venda= somat
        cu= i
    
a= input().strip()
p= ano.index('%s'%a)

if fiat[p]> eita:
    eita= fiat[p]
    marca= 0

if ford[p]> eita:
    eita= ford[p]
    marca= 1

if gm[p]> eita:
    eita= gm[p]
    marca= 2
    
if wolkswagen[p]> eita:
    eita= wolkswagen[p]
    marca= 3



print(f'A fabricante que mais vendeu em {a} foi a {carros[marca]} com {eita} mil unidades.')

print(f'O ano de maior volume geral de vendas foi {ano[cu]} com {venda} mil unidades.')

print('A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')
print(f'A Fiat vendeu em média {round(soma1/6, 2)} unidades por ano.')
print(f'A Ford vendeu em média {round(soma2/6, 2)} unidades por ano.')
print(f'A GM vendeu em média {round(soma3/6, 2)} unidades por ano.')
print(f'A Wolkswagen vendeu em média {round(soma4/6, 2)} unidades por ano.')

