placar= 0

mensagem= input("Por favor, entre com um nome: ").lower()
nome= input("Por favor, entre com um segundo nome: ").lower()

for char in mensagem:
    if char in "aeiou":
        placar+= 1
    if char in "amor":
        placar+= 2
for char in nome:
    if char in "aeiou":
        placar+= 1
    if char in "amor":
        placar+= 2

if placar >10:
    print("Voces são compativeis.")
else:
    print("Esqueça essa pessoa.")
