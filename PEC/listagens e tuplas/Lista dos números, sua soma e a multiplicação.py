
    
def main():
    a= []
    soma = 0
    outro= 1

    for i in range(10):
        b= int(input())
        a.append(b)
        soma+= a[i]
        outro*= a[i]

    print(a)
    print('%.d'% soma)
    print('%.d'% outro)
    
if __name__== "__main__":
  main()
