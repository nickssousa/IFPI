score= 0
print('''
Q1 - Qual a capital do Brasil?
a - Buenos Aires
b - Brasilia
c - Roma
''')
resposta= input().lower()

if resposta == "a":
    print("Respota errada.")
elif resposta == "b":
    print ("Correto!! :)")
    score= score +1
elif resposta == "c":
    print ("Respota errada.")
else:
    print("Você não escolheu a, b ou c :(")


print('''
Q2 - Qual a capital da Argentina?
a - Buenos Aires
b - Brasilia
c - Roma
''')
resposta= input().lower()

if resposta == "a":
   print ("Correto!! :)")
   score= score +1
elif resposta == "b":
    print("Respota errada.")
elif resposta == "c":
    print("Respota errada.")
else:
    print("Você não escolheu a, b ou c :(")


   
print('''
Q3 - Qual a capital do Peru?
a - Montevidéu
b - Buenos Aires
c - Lima
''')
resposta= input().lower()

if resposta == "a":
    print("Respota errada.")
elif resposta == "b":
    print("Respota errada.")
elif resposta == "c":
    print ("Correto!! :)")
    score= score +1
else:
    print("Você não escolheu a, b ou c :(")


print('''
Q4 - Qual a capital do Uruguai?
a - Montevidéu
b - Cairo
c - Lima
''')
resposta= input().lower()

if resposta == "a":
    print ("Correto!! :)")
    score= score +1
elif resposta == "b":
    print("Respota errada.")
elif resposta == "c":
   print("Respota errada.")
else:
    print("Você não escolheu a, b ou c :(")



print('''
Q5 - Qual a capital da Itália?
a - Veneza
b - Roma
c - Piza
''')
resposta= input().lower()

if resposta == "a":
    print("Respota errada.")
elif resposta == "b":
    print ("Correto!! :)")
    score= score +1
elif resposta == "c":
   print("Respota errada.")
else:
    print("Você não escolheu a, b ou c :(")


if score == 5:
    print("Acertou tudo parabens!")
elif score == 3 or 4:
    print("Foi bem no desafio.")
elif score == 0 or 1 or 2:
    print("Tente de novo")
