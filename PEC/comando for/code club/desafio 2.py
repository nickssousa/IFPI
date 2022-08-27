#lista de letras para criptografar
alfabeto= "aeioubcdfghjklmnopqrstvwxyz"

#capture a mensagem do usuário
mensagem= input("Por favor, entre com a mensagem a ser criptografada: ").lower().strip()

#está variável armazenará a mensagem criptografada
mensagemCriptografada= ""

#capture a chave sercreta
chave= int(input("Entre com uma chave: "))

#percorra cada cartacter na mensagem
for char in mensagem:
    if char in alfabeto:

        #encontre a posição de caracter em alfabeto
        #por exemplo, 'a' está na posição 0, 'e' está na posição 4 e etc.
        posicao= alfabeto.find(char)

        #some a chave secreta para encontrar a posição da letra criptografada
        #% 26 significa 'volte para 0 quando você chegar no 26'
        novaPosicao= (posicao+ chave)% 26

        #acrescente a letra descriptografada à mensagem
        #a letra criptografada está em alfabeto na novaPosicao
        mensagemCriptografada= mensagemCriptografada+ alfabeto[novaPosicao]

        chave+= 1

    else:
        #alguns caracteres (por exemplo '$') não estão no alfabeto,
        #então simplismente adicione a letra criptografada à mensagem
        mensagemCriptografada= mensagemCriptografada+ char

print("Sua mensagem criptografada é:", mensagemCriptografada)
