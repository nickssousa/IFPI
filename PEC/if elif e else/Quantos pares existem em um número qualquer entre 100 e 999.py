z= int(input())
x= 0

if 99< z < 1000:
    a = z // 100
    b= (z //10) %10
    c= z% 10
    if a % 2 ==0:
        x= x+1
    if b % 2 ==0:
        x = x+1
    if c%2 ==0:
        x= x+1

print(f'{x}')
