lista= {}
x= int(input())
codigo= 0

for i in range(x):
    nome= input().strip()
    cidade= input().strip()
    estado= input().strip()
    a= cidade+"("+estado+")"
    telefone= input().strip()
    lista[codigo]= nome, a, telefone
    codigo+= 1
    
for codigo in lista:
    aqui1, aqui2, aqui3 = lista[codigo]
    print("{:<25}{:<30}{:<10}".format(aqui1, aqui2,aqui3))
