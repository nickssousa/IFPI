a = int(input())
inverso = 0 
     
while a != 0:    
    b= a% 10
    inverso = inverso* 10+ b    
    a= a// 10    
   
  
print(inverso) 
