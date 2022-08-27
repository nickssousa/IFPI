a= float(input())
b= input().upper().strip()
x= float(input())
z= input().upper().strip()

#c, far
if b== 'F':
    c= ((a-32)*(5/9))
    far= (a, b)    
    
#y, fari
if z== 'F':
    y= ((x-32)*(5/9))
    fari= (x, z)

#a, cel
if b== 'C':
    d= a
    cel= (a, b)    

#x, cels
if z== 'C':
    v= x
    cels= (x, z)

if (b== 'F') and (z== 'F'):
    if c>y:
        print(far)
    if y>c:
        print(fari)

if b== 'F' and z== 'C':
    if c>x:
        print(far)
    if x>c:
        print(cels)

if b == 'C' and z == 'F':
    if d> y:
        print(cel)
    if y>d:
        print(fari)

if b == 'C' and z == 'C':
    if d> v:
        print(cel)
    if v> d:
        print(cels)



