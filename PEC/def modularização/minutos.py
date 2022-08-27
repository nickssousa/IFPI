def coisa(x):
    return x//60
def outro(x):
    y= x%60
    x= y
    return x
minutos= int(input())
print(f'{coisa(minutos)}:{outro(minutos)}')
