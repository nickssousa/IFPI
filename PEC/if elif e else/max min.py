a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

def max(u, v, x, y, z):
    if v< u and x< u and y< u and z< u:
        return u
    elif u< v and x< v and y< v and z< v:
        return v
    elif u< x and v< x and y< x and z<x:
        return x
    elif u< y and v< y and x< y and z< y:
        return y
    else:
        return z

def min(u, v, x, y, z):
    if v> u and x> u and y> u and z> u:
        return u
    elif u> v and x> v and y> v and z> v:
        return v
    elif v> x and u> x and y> x and z> x:
        return x
    elif v> y and x> y and u> y and z> y:
        return y
    else:
        return z

print(f'{max(a, b, c, d, e)}')
print(f'{min(a, b, c, d, e)}')
