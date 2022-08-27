def data(a, b, c, g, h, i):
    if a< g:
        h = h +1
        if b< h:
            i= c - (i+ 1)
    else:
        i = c - i
    return i

x= int(input())
y= int(input())
z= int(input())

d= int(input())
e= int(input())
f= int(input())

print(f'{data(x, y, z, d, e, f)}')
