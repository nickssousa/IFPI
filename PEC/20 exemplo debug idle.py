def func_a():
    return 'A'

def func_b():
    return 'B'

def func_c():
    return 'C'

def func_abc():
    a = func_a()
    b = func_b()
    c = func_c()
    return a + b + c

def main():
    resultado = func_abc()
    print(resultado)

if __name__ == '__main__':
    main()
