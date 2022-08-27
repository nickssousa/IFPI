def main():
    n = int(input())
    a, b = 0, 1
    for x in range(0, n-1):
        print(a, end=', ')
        a, b = b, a+b
    print(a)
    
if __name__== "__main__":
  main()
