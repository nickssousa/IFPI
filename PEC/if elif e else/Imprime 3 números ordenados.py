a= int(input())
b= int(input())
c= int(input())

if a>b and a>c:
    if b> c:
        print('''%d
%d
%d'''% ( c, b, a))
    else:
        print('''%d
%d
%d'''% ( b, c, a))
        
elif b>a and b>c:
    if a> c:
         print('''%d
%d
%d'''% ( c, a, b))
         
    else:
         print('''%d
%d
%d'''% ( a, c, b))
        
else:
    if a>b:
         print('''%d
%d
%d'''% ( b, a, c))
         
    else:
         print('''%d
%d
%d'''% ( a, b, c))
    
