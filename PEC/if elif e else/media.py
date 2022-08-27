x= float(input())
y= float(input())
z= float(input())
media= (x+y+z)/3

if 8 < z:
    media= media + 1
    if 10<media:
        print(f'A media é 10')
    else:
        print('A media é %.1f'%(media))
else:
    print('A media é %.1f'%(media))
    
