from random import *

#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!
=======

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

    _____     _____    _____
   |     |   |     |  |     |
   | [1] |   | [2] |  | [3] |
   |    o|   |    o|  |    o|
   |_____|   |_____|  |_____|

   Escolha uma porta (1, 2 ou 3):
''')

#deixe o jogador fazer 3 tentativas
score= 0
for attempt in range(3):
    print("\nEscolha um porta (1, 2 ou 3):")

    #pegue a porta escolhida e armazene como um número inteiro (int)
    portaEscolhida= input()
    portaEscolhida= int(portaEscolhida)
    
    
    #escolha aleatoriamente a porta que esconde o premio (entre 1 e 3)
    portaCerta = randint(1,3)

    #mostre ao jogador qual porta ele escolheu e qual era a porta certa
    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    #o jogador ganha se o numero da porta escolhida e o da porta certa forem o mesmo
    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score+= 1

    else:
        print("Que peninha!")

print(f'Você acertou {score} vezes')
   
