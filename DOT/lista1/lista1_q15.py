soma= 0

def func(valor):
    b= (valor**2+1)/(valor+3)
    return b

while True:
    try:
        a= int(input('Digite um número inteiro posítivo: '))
        if a> 0:
            for i in range(1, a+1):
               soma+= func(i)
               
            print(soma)
            break
            
        else:
            print('Digite um número posítivo.')
    
    except:
        print('Caractere inválido. Digite novamente.')

