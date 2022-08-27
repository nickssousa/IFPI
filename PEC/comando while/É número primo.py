def main():
    n = int(input())
    a= 0
    b= 0
    for x in range(1, n+1):
        if n%x== 0:
            b+= 1
    if b== 2:
        print('True')
    else:
        print('False')
    
if __name__== "__main__":
  main()
