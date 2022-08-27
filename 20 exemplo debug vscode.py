def teste_numero(n):
    a = 0
  
    for b in range(1, n):
        if n % b == 0:
            a += b

    return n == a

def main():
    while True:
        a = int(input('Digite um número (0 para fim): '))
        if a == 0: break
        print(f'O teste para {a} é {teste_numero(a)}')

if __name__ == '__main__':
    main()
