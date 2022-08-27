def divisores(num):
    for i in range(1, int(num/2+1)):
        if num % i == 0: 
           yield i
    yield num

while True:
    try:
        a= int(input('Digite um numero: '))
        while a<= 0:
            a= int(input('Digite um numero positivo: '))
    
        d = divisores(a)
        print('Seus divisores são:')
        [print(i) for i in d]
        break

    except:
        print('Caractere invalido. Tente novamente.')


