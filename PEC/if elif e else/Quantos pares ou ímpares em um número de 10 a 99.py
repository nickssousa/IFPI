x= int(input())

if 9<x<100:
    a= x//10
    b= x%10
    if a%2 ==0 and b%2 ==0:
        print('Nenhum dígito é ímpar.')
    elif a%2 ==0 or b%2 ==0:
        print('Apenas um dígito é ímpar.')
    else:
        print('Os dois dígitos são ímpares.')

