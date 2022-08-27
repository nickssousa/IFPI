a= float(input())
b= input().upper().strip()
x= float(input())
z= input().upper().strip()

if z!= b:
    if b== 'F':
        a= (a-32)*5/9
    else:
        a= (a*(9/5)) + 32

c= round(a+x, 4)
aqui= (c,z)
print(aqui)
    
