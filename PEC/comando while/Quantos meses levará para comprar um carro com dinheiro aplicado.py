def main():
    a= float(input())
    b= 10000
    mes= 0
    while a>b:
        b= b+ (b*0.007)
        a= a+ (a*0.004)
        mes+=1

    print(mes)

if __name__== "__main__":
  main()
