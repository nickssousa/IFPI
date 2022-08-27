
alunos = {
    100: ('Pedro', [8.5, 8.0]),
    101: ('Bia', [7.0, 9.5]),
    102: ('Rafael', [6.5, 8,5]),
}


# (C)RUD
def criar():
    # o código é autoincremento
    codigo = max(alunos.keys()) + 1
    # ler o nome do aluno
    nome = input('Nome do aluno: ')
    # ler a nota e coloca em uma lista de notas
    notas = [float(input("Nota do aluno: "))]
    # empacota nome e notas como um aluno
    aluno = (nome, notas)
    # adiciona o aluno ao dicioário
    alunos[codigo] = aluno
    input('Registro Incluído. Pressione qualquer tecla para contunuar...')


# C(R)UD
def ler(codigo):
    # carrega os dados do dicionário e desempacota nas variáveis nome e nota
    nome, nota = alunos[codigo]
    # retorna as variáveis desempacotadas
    return nome, nota


# CR(U)D
def atualizar(codigo):
    # carrega dados do aluno definido pelo código
    nome, nota = ler(codigo)
    # ler um novo nome para um aluno na variável auxiliar
    aux = input(f'Nome do aluno (atual: {nome}): ')
    # se o valor lido para o nome for vazio, ignora e mantém o mesmo valor
    if aux != '':
        # se for lido um valor válido, atualiza o campo nome
        nome = aux
    # usa a mesma variável auxiliar para ler uma nota
    aux = input(f'Nota do aluno (atual: {nota}): ')
    # se o valor lido para a nota for vazio, ignora e mantém o mesmo valor
    if aux != '':
        # se for uma nota válida, pergunta se é uma nova nota para ser incluída
        nova = input(f'Incluir nova nota? (S, N): ')[0].upper() == 'S'
        if nova:
            # se o usuário confirma que é uma nova nota
            # adiciona a nota na lista de notas do aluno
            alunos[codigo][1].append(float(aux))
            print('Nota incluída com sucesso.')
        else: # se não é uma nova nota, o usuário deseja alterar uma nota existente
            # mostra as notas atuais
            print('Notas Atuais: ', alunos[codigo][1])
            # e ler o índice da nota que deseja alterar
            i_nota = int(input('Posição para alterar?: '))
            # faz a alteração da nota no índice lido
            alunos[codigo][1][i_nota] = float(aux)
            print('Nota Alterada com sucesso.')
    # atualiza os dados no dicionário aluno
    alunos[codigo] = (nome, nota)
    input('Registro Atualizado. Pressione qualquer tecla para contunuar...')


# CRU(D)
def apagar(codigo):
    # ler o código para apagar. Como as notas não são relevantes agora, coloca em uma variável _
    nome, _ = ler(codigo)
    # pegue uma confirmação do usuário para excluir
    confirma = input(f'Deseja realmente apagar {nome}? (S, N): ')[0].upper() == 'S'
    if confirma:
        # se confirmado, apaga o registro
        del alunos[codigo]
        input('Registro Apagado. Pressione qualquer tecla para contunuar...')


def listar_alunos():
    # imprime uma listagem com todos os alunos
    print('=' * 10, 'Listando Todos Alunos', '=' * 10)
    qtd = 0
    # código recebe todas as chaves do dicionário aluno
    for codigo in alunos:
        # ler os dados do aluno
        nome, nota = ler(codigo)
        print('-' * 30)
        print(f'Código do Aluno: {codigo}')
        # imprime os dados
        print(f'Nome: {nome}')
        print(f'Nota: {nota}')
        qtd += 1
    if qtd == 0:
        print('<<< Nenhum aluno para mostrar >>>')
    else:
        print(f'{qtd} aluno(s) exibidos no relatório.')
    print('=' * 10, 'Fim da Listagem de Todos Alunos', '=' * 10)
    input('Pressione qualquer tecla para continuar....')



def menu():
    # mostra um menu de opções e faz a leitura da opção desejada
    while True:
        print('1 - (C) Incluir aluno')
        print('2 - (R) Ler aluno')
        print('3 - (U) Atualizar aluno')
        print('4 - (D) Apagar aluno')
        print('5 - Listar Todos')
        print('0 - Fim do Programa')
        print('=' * 30)
        opcao = int(input('Digite sua opção: '))
        if opcao in (1, 2, 3, 4, 5, 0):
            return opcao
        else:
            print('Opção Inválida')


def main():
    while True:
        op = menu()
        if op == 1:  # create
            criar()
        elif op == 2:  # read
            codigo = int(input('Código para carregar: '))
            if codigo in alunos:
                nome, nota = ler(codigo)
                print('-' * 30)
                print(f'Nome do Aluno: {nome}')
                print(f'Nota do Aluno: {nota}')
                print('-' * 30)
            else:
                print(f'Aluno não existe aluno com código {codigo}.')
        elif op == 3:  # update
            codigo = int(input('Código para Atualizar: '))
            if codigo in alunos:
                atualizar(codigo)
            else:
                print(f'Aluno não existe aluno com código {codigo}.')
        elif op == 4:  # delete
            codigo = int(input('Código para Remover: '))
            if codigo in alunos:
                apagar(codigo)
            else:
                print(f'Aluno não existe aluno com código {codigo}.')
        elif op == 5:  # listar todos
            listar_alunos()
        elif op == 0:  # fim do programa
            print('Fim do programa.')
            break
        else:
            pass


if __name__ == '__main__':
    main()
