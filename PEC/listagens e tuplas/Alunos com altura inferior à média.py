def main():
    nome= []
    idade= []
    altura= []
    soma= 0
    
    for i in range(30):
        x= input().strip()
        y= int(input())
        z= float(input())
        nome.append(x)
        idade.append(y)
        altura.append(z)
        soma+= z
        
    media= round(soma/30, 2)
    
    print("MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
    for i in range(30):
        if idade[i] > 13:
            if altura[i] < media:
                print(nome[i])
            
if __name__== "__main__":
  main()
