def main():
    a= int(input())
    b= int(input())
    ano= 0
    c= max(a, b)
    d= min(a, b)
    while c>=d:
        d= d+ (d*0.03)
        c= c+ (c*0.02)
        ano+=1

    print(ano)

if __name__== "__main__":
  main()
