while True:
    try:
        a= float(input("Digite um numero: "))
        print(a*3)
        b= input("Deseja continuar? S/N:\n").lower()
        if b == 'n':
            break
        elif b == 's':
            pass
        else:
            print("Caractere invalido. Digite novamente.")
    
    except:
        print("Caractere invalido. Digite novamente.")