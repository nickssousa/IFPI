def eita(n):  
    if n> 1:
        for i in range(2, n):
            if (n% i) == 0:
                break
        else:
            print(n)
 
    else:
        pass
         
def main():
    a= int(input())
    b= int(input())
    
    d= max(a,b)
    e= min(a,b)

    for x in range(e,d+1):
        if eita(x)== True:
            print(x)
        
if __name__== "__main__":
  main()
