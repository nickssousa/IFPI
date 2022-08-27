    
a= 0
b= 0
for n in range(100):
    eita= int(input())
    if not eita%2 ==0:
        b += 1
    if eita%2 == 0:
        a += 1
print(f'{a}')
print(f'{b}')

