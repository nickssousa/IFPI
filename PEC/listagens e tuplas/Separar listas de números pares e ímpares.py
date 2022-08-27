def main():
    a= []
    b= []
    c= []
    
    for i in range(20):
        x= int(input())
        a.append(x)
        if x%2==0:
            b.append(x)
        else:
            c.append(x)
    print(a)
    print(b)
    print(c)
    
if __name__== "__main__":
  main()
