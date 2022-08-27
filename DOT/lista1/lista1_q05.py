def ideal(a, b):
    if a == 2:
        return (62.1* b)- 44.7
    if a == 1:
        return (72.7* b)- 58


while True:
    try:
        sexo= int(input("Digite o sexo da pessoa:\n 1- Masculino\n 2- Feminino:\n "))
        if sexo == 1 or sexo == 2:
            break
        else:
            print("Digite 1 para masculino ou 2 para feminino")
    
    except:
        print("Digite um número valido")

while True:
    try:
        altura= float(input("Digite a altura: "))
        break
    except:
        print("Digite uma altura válida.")

print(f'seu peso ideal é {ideal(sexo, altura)}')