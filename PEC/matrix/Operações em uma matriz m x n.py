soma= 0
primeiro= 0
coluna= 0
maior= 0
menor= 99999999

a= int(input())
b= int(input())


# Captura os valores de cada célular do quadrado
for i in range(a):
    for j in range(b):
        valor = int(input().strip())
        soma+= valor
            
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

        if i== 0:
            primeiro+= valor

        if j== (b-1):
            coluna+= valor
 
tupla= ( primeiro,coluna,round((soma/(a*b)), 4),menor,maior)
print(tupla)
