from random import *
jogando = True
print('''
Vinte e um!
===========
tente fazer exatamente 21 pontos!
''')

x= 0
y= 0
while jogando == True:
    b= randint(1,10)
    print("Seu proximo número é", b)
    x+= b
    print("Sua pontuação agora é", x)

    print("\nGostaria de somar mais um número? (s/n)")
    a= input().lower()

    if a == 'n' or a == 'nao':
        jogando = False

if x == 21:
    print("Sua pontuação final é", x)
    print("VOCÊ VENCEU!")
else:
    print("Sua pontuação final é", x)
    print("Que pena!")
