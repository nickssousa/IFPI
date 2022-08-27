from random import *
executa = True

minino= ["Vitu", "Cleber", "Valdemar", "Bisnaga", "Rodinei"]
minina= [ "Josefa", "Arnalda", "Caramelo", "Buneca", "Tata"]
           

print("Gerador de nomes para animais de estimação")
print("------------------------------------------")

nome= input('''Qual o sexo do animal?
    1- Macho
    2- Fêmea
     ''')

print('''
menu
    c= obter um nome
    a= adicionar um nome
    d= remover um nome
    p= imprimir os nomes
    q= sair''')

while executa == True:
    if nome == '1':
        menuChoice= input("\n>_").lower()

        #'c' para um cumprimento
        if menuChoice == 'c':
            print("Você deve chamar seu animal de ", choice(minino))

        #'a' para adicionar um hobby
        elif menuChoice == 'a':

            itemToAdd= input("Adicionar o nome: ")

            if itemToAdd in minino:
                print("O nome ja esta na lista")
            else:
                minino.append(itemToAdd)

        #'d' para remover um hobby
        elif menuChoice == 'd':
            itemToDelete= input("Insira o nome a ser removido: ")

            #só remove um item se ele estiver na lista
            if itemToDelete in minino:
                minino.remove(itemToDelete)
            else:
                print("O nome não está na lista!")

        #'p' para imprimir a lista de hobbies
        elif menuChoice == 'p':
            print(minino)

        #'q' para sair
        elif menuChoice == 'q':
            executa = False

        else:
            print("Insira uma opção valida")

    if nome == '2':
        menuChoice= input("\n>_").lower()

        #'c' para um cumprimento
        if menuChoice == 'c':
            print("Você deve chamar seu animal de ", choice(minina))

        #'a' para adicionar um hobby
        elif menuChoice == 'a':

            itemToAdd= input("Adicionar o nome: ")

            if itemToAdd in minina:
                print("O nome ja esta na lista")
            else:
                minina.append(itemToAdd)

        #'d' para remover um hobby
        elif menuChoice == 'd':
            itemToDelete= input("Insira o nome a ser removido: ")

            #só remove um item se ele estiver na lista
            if itemToDelete in minina:
                minina.remove(itemToDelete)
            else:
                print("O nome não está na lista!")

        #'p' para imprimir a lista de hobbies
        elif menuChoice == 'p':
            print(minina)

        #'q' para sair
        elif menuChoice == 'q':
            executa = False

        else:
            print("Insira uma opção valida")
