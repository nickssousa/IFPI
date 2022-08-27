def coisa(numero):
    a= numero % 10
    numero= numero //10
    b= numero %10
    numero= numero //10
    c= numero% 10
    numero= numero //10
    d= numero %10
    numero_invertido= (a*1000) + (b*100) + (c*10) + d
    return numero_invertido
x= int(input())


print(coisa(x))
