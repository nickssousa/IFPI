def aqui(x):
    soma= 0
    for i in range(1, x+1):
        soma+= 1/i
    
    return soma


while True:
    try:
        S= int(input("Digite um valor inteiro positivo: "))
        if S > 0:
            print(aqui(S))
            break
        else:
            print("Digite um número positivo.")
        
    except:
        print("Digite um caráctere válido.")

