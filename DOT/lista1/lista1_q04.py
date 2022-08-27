def media(a, b):
    return (a+b)/ 2

while True:
    try:
        c= float(input("Digite o valor da primeira nota: "))
        d= float(input("Digite o valor da segunda nota: "))
        if media(c, d) > 6.0:
            print("Parabens, você foi aprovado.")
            break
        else:
            print("Sinto muito, você foi reprovado.")
            break

    
    except:
        print("Digite um valor válido.")