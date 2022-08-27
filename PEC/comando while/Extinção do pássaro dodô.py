def main():
    a= int(input())
    f= a*0.1
    b= a*0.06
    c= a*0.01
    ano= 1600
    a= a-b+c
    print("%d,%d,%d,%d"%(ano, round(c,0), round(b,0), round(a,0)))
    while a > f:
        d= a*0.06
        e= a*0.01
        a= a-d+e
        ano+= 1
         
        print("%d,%d,%d,%d"%(ano, round(e,0), round(d,0), round(a,0)))

if __name__== "__main__":
  main()
