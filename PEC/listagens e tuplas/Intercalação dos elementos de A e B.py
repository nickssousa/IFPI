def main():
    a= []
    b= []
    c= []
    
    for i in range(25):
        x= int(input())
        a.append(x)

    for i in range(25):
        z= int(input())
        b.append(z)

    for i in range(25):
        c.append(a[i])
        c.append(b[i])

    print(a)
    print(b)
    print(c)
    
if __name__== "__main__":
  main()
