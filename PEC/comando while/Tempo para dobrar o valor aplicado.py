a= float(input())
b= float(input())

b= b/100
c= 2*a
anos= 0

while c > a:
    a= a+(a*b)
    anos+= 1

print(anos)
