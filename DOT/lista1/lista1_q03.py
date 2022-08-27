from string import whitespace


def celsius(Temp):
    return ((Temp-32)/9)*5

while True:
    try:
        F= float(input("Dogite uma temperatura em Fahrenheit: "))
        break

    except:
        print("Digite um valor válido")

print(f'O valor dessa temperatura em celsius é {celsius(F)}')