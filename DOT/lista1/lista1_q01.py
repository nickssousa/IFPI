def par_impar(x):
    if x % 2 == 0:
        return True

    else:
        return False

num = int(input("\nDigite um número: "))

if par_impar(num):
    print("\nO número %d é par." % num)
else:
    print("\nO número %d é ímpar." % num)