def main():
    a= []
    b= []
    c= []
    
    for i in range(20):
        x= int(input())
        a.append(x)

    for i in range(20):
        z= int(input())
        b.append(z)

    for i in range(20):
        c.append(a[i] + b[i])

    print(a)
    print(b)
    print(c)
    
if __name__== "__main__":
  main()
