def main():
    a= []
    cont= 0
    b= 0
    c= 0
    d= []
    ma= 0
    mi= 9999999999
    soma= 0
    
    while True:
        x= int(input())

        if x== 0:
            break

        else:
            a.append(x)

    for element in a:
        cont += 1
    
    for element in a:
        d.insert(0, element)

    for element in a:
        if element < mi:
            mi = element

    for element in a:
        if element> ma:
            ma= element

    for element in a:
        soma+= element

    print(a)
    print(cont)
    print(d)
    print(mi)
    print(ma)
    print(soma)
    

if __name__== "__main__":
  main()
