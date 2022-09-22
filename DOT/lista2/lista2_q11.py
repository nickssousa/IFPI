def cadastrar_nome():
  nome= input("Digite o nome: ").upper()
  lista.append(nome)


def pesquisar_nome():
  pesquisa = input("Digite o nome que deseja procurar: ").upper()
  for i in lista: 
    if(i == pesquisa) : 
        print ("Nome consta na lista")

    else:
      print("Nome não consta na lista")

def deletar_nome():
  delete = input("Digite o nome que deseja apagar: ").upper()
  for i in lista: 
    if(i == delete) : 
        lista.remove(delete)
        print("Nome apagado")

    else:
      print("Nome não consta na lista") 

print('''MENU:
1 - Cadastrar nome:
2 - Pesquisar nome:
3 - Listar todos os nomes:
4 - Excluir nome:
5 - Alterar nome:
0 - Sair do programa:
------------------------------------''')
lista= []

while True:
  try:
    a= int(input("Digite uma opção: "))
    if a == 1:
      cadastrar_nome()
    
    elif a == 2:
      pesquisar_nome()

    elif a == 3:
      print(lista)

    elif a == 4:
      deletar_nome()

    elif a == 0:
      break

    else:
      print("Digite um valor no menu.")
    
  except:
    print("Digite um valor no menu: ")
