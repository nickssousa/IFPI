def perimetro(lado):
    return lado*3

def area(papel):
    return papel**2

while True:
    try:
        l= int(input("\nDigite o número de lados do seu polígono\n3- Para triângulo.\n4- Para quadrado.\n5- Para pentágono.\n: "))
        while l>5 or l<3:
            l= int(input("O número deve ser entre 3 e 5: "))

        medida= float(input("Agora digite o valor do lado do polígono: "))
        if l == 3:
            print("TRIÂNGULO.")
            print(f'E o perímetro dele é {perimetro(medida)}')
            break
        
        elif l == 4:
            print("QUADRADO.")
            print(f'E a área dele é {area(medida)}')
            break
        
        elif l == 5:
            print("PENTÁGONO.")
            break
    
    except:
        print("Digite 1, 2 ou 3")
