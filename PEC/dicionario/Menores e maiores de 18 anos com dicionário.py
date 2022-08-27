lista= {}
lista2={}
codigo= 0
outro= 0

for i in range(20):
    nome= input().strip()
    idade= int(input().strip())
    cpf= input().strip()
    
    if idade<18:
        lista[codigo]= nome, idade, cpf
        codigo+= 1
        
    else:
        lista2[outro]= nome, idade, cpf
        outro+= 1

print("========== MAIORES DE 18 ANOS ==========")
for codigo in lista2:
    aqui1, aqui2, aqui3 = lista2[codigo]
    print(f'{aqui1};{aqui2};{aqui3}')

print("========== MENORES DE 18 ANOS ==========")
for outro in lista:
    aqui4, aqui5, aqui6= lista[outro]
    print(f'{aqui4};{aqui5};{aqui6}')
