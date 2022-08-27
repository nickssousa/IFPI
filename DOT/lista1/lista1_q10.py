for i in range(4):
    try:
        a= int(input("Digite um número: "))
        b= int(input("Digite um número: "))
        c= int(input("Digite um número: "))
        d= int(input("Digite um número: "))
        print(max(a, b, c, d))
    
    except:
        print("digite um valor valido")