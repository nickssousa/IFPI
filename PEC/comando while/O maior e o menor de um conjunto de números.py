b= 0
c= 99999999

while True:
    a= int(input())
    if a ==0:
        break
    else:
        if a>b:
            b=a
        if a<c:
            c=a
if c == 99999999: pass

else:
    print(b)
    print(c)
        
