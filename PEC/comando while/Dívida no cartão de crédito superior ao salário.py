
salario= float(input())
divida= float(input())
mes= 10
ano = 2016
while salario>divida:
    divida = divida+ (divida*0.15)
    mes+= 1
    if mes ==3:
        salario= salario+ (salario*0.05)

    if mes == 13:
        mes = 1
        ano+= 1
print(f'{mes}/{ano}')    
    
    
    
