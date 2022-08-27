print('''
Qual é a tradução de yellow?
a - verde
b - amarelo
c - azul
''')
resposta= input().lower()

if resposta == "a":
    print(" Não, verde é green :(")
elif resposta == "b":
    print ("Correto!! :)")
elif resposta == "c":
    print ("Não, azul é blue! :(")
else:
    print("Você não escolheu a, b ou c :(")
