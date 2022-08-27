'''
    DEFINIÇÃO: INDENTAÇÃO OU ENDENTAÇÃO
    ===================================
    
    Em inglês nós temos o verbo "to indent" que
    significa encaixar.

    Em português a palavra "indentar" ainda é,
    para muitos, um neologismo.

    É mais comum dicionários de português trazer
    a palavra "endentar", que é derivada de "dente".

    O "dente" pode ser humano, a estrutura da maxila
    e da mandíbula, que realiza a mastigação.

    Mas também pode ser uma saliência ou ponta
    em objetos construídos ou elaborados pelo
    homem. "dentes de uma engrenagem"

    Enfim, para programação, "Indentar" ou "Endentar"
    é um recuo do texto em relação à margem;
    inserindo (ou não) um espaço entre
    a margem e o comando.


    TABULAÇÃO x ESPAÇO EM BRANCO
    ============================

    Se olhar na tabela ASCII temos os caracteres:
    
    TECLA DE TH OU TAB (código decimal 09):
    ---------------------------------------

    é uma tabualação horizontal.
    Vem de tabular, deslocar parte de um texto
    através de vários espaços *predefinidos* para
    melhor visualização.

    TECLA DE ESPAÇO (código decimal 32):
    ------------------------------------

    é um espaço em branco.
    Lugar vazio que pode ser ocupado.

    Em Python, a indentação pode ser feita com
    qualquer quantidade de espaços ou tabulação.
    Por padrão, devemos usar 4 espaços para
    fazer a indentação dos blocos de comandos.
        
    Alguns editores de texto próprios para programação convertem automáticamente
    um TAB em 4 espaços em branco. É o caso do IDLE.
'''

print('Comando 1')
print('Comando 2')
print('Comando 3')
print('Comando 4')
print('Comando 5')


if True:
    print('Comando 6')
    print('Comando 7')

print('Comando 8')


if True: print('Comando 9')

if False:
    print('Comando 10 (não executa)')
    print('Comando 11 (não executa)')

if False: print('Comando 12 (não executa')

print('Comando 10')
print('Comando 11')
print('Comando 12')


for i in range(3):
    print(f'Comando 13 (i={i})')

for j in range(3): print(f'Comando 14 (j={j})')


def e_par(n): return n % 2 == 0

for k in range(1, 11): # k vai de 1 a 10
    if not e_par(k): print(f'Comando 15 (k={k})')

    if e_par(k):
        print(f'Comando 16 (k={k})')


for i in range(3):
    for j in range(3):
        print(f'Comando 17 (i={i},j={j})')
        print(f'Comando 18 (i={i},j={j})')
    print(f'Comando 19 (i={i},j={j})')
    print(f'Comando 20 (i={i},j={j})')

print('Último comando')
