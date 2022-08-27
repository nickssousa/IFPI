def main():
    a= int(input())
    c= 0
    
    while a != 0:    
        b= a% 10
        c = c+ b    
        a= a// 10 

    print(c)

if __name__== "__main__":
  main()
