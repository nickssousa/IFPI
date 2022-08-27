def main():
    n = int(input())
    a= 1
    for x in range(2, n+1):
        a+= (1/x)
    print("%.4f"% a)
    
if __name__== "__main__":
  main()
