def main():
    a= []
    b= []
    c= []
    e= 0
    g= 0
    x= int(input())

    for i in range(x):
        a.insert(0, round(float(input().strip()), 4))
    print(a)

    for i in range(x):
        b.append(round(float(input().strip()), 1))
        e+= b[i]
    print(b)

    if e ==0:
        print("SEM NOTAS")
    else:
        print(round((e/x), 1))

    for i in range(x):
        f= input().strip()
        if f in 'AEIOUaeiou':
            g+= 1
        
        if f in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            c.append(f)
        
    print(g)   
    print(c)
    
if __name__== "__main__":
  main()
