def main():
    while True:
        print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
        a= float(input())

        if a== 1:
            print('1 - Olá. Como vai?')

        if a== 2:
            print('2 - Vamos estudar mais.')

        if a== 3:
            print('3 - Meus Parabéns!')

        if a== 0:
            print('0 - Fim de serviço.')
            break

        if a not in (0,1,2,3):
            print('Opção inválida.')
                

if __name__== "__main__":
  main()
