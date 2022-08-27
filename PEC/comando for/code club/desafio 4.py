senhas={
    "programador": "claralate"
    }

nome= input("Nome: ")
password= input("Senha: ")

if nome in senhas and password == senhas[nome]:
    print("BEM-VINDO PROGRAMADOR")

else:
    print("Senha ou nome invalido")
