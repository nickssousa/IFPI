b= 0
coisa= 0

while True:
    a= int(input())
    if a != 0:
        b+= a
        coisa +=1
        
    if a == 0: break
    
if coisa== 0: pass
else: print('%.2f'%(b/coisa))
