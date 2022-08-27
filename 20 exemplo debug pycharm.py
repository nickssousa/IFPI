"""
    Leia um texto pelo teclado e informe:
    - a quantidade de vogais
    - a quantidade de consoantes
    - a quantidade de números
    - a quantidade de símbolos
"""


def e_letra(c):
    return 'A' <= c <= 'Z'
    # return 'A' <= c.upper() <= 'Z'


def e_numero(c):
    return c in ' O13456789 '
    # return c in '0123456789'


def e_vogal(c):
    return c in 'AeIi0oUu'
    # return c in 'AaEeIiOoUu'


def e_consoante(c):
    return e_letra(c) and not e_vogal(c)


def e_simbolo(c):
    return not (e_letra(c) or e_numero(c))


def main():
    texto = 'Em 22 de abril de 1500, Pedro Álvares Cabral chega à Ilha de Vera Cruz (o Brasil).'
    qtd_vogal = qtd_consoante = qtd_numero = qtd_simbolo = 0
    for c in texto:
        if e_vogal(c):
            qtd_vogal += 1
        elif e_consoante(c):
            qtd_consoante += 1
        elif e_numero(c):
            qtd_numero += 1
        elif e_simbolo(c):
            qtd_simbolo += 1

    print(f'Texto: {texto}')
    print(f'Vogais: {qtd_vogal}')
    print(f'Consoantes: {qtd_consoante}')
    print(f'Números: {qtd_numero}')
    print(f'Símbolos: {qtd_simbolo}')
    print(f'Total: {len(texto)}')


if __name__ == '__main__':
    main()
