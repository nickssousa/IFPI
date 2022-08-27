def main():
    a= []
    cont= 0
    True

    while True:
        x= int(input())
        
        if x== 0:
            break
        else:
            a.append(x)

    z= int(input())
    for i in range(len(a)):
        if z == a[i]:
            cont+= 1

    print(a)
    print(z)
    print(cont)

if __name__== "__main__":
  main()
