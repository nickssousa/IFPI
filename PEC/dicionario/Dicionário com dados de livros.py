dicionario= {}
codigo= 101

while True:
    nome1= input().strip()
    if not nome1:
        break
    else:
        nome2= input().strip()
        nome3= input().strip()
        nome4= float(input())
        dicionario[codigo]= nome1, nome2, nome3, nome4
        codigo+=1
    
for codigo in dicionario:
    aqui1, aqui2, aqui3, aqui4 = dicionario[codigo]
    print(f'Código: {codigo}\nTítulo: {aqui1}\nISBN: {aqui2}\nAutor: {aqui3}\nPreço: {aqui4}0')
