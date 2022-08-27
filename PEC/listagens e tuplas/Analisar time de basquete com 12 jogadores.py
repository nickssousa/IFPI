def main():
    nome= []
    altura= []
    soma= 0
    
    for i in range(12):
        x= input().strip()
        z= float(input())
        nome.append(x)
        altura.append(z)
        soma+= z
        
    c= altura.index(max(altura))
    print("JOGADOR MAIS ALTO DO TIME")
    print(nome[c])
    print('%.2f'% altura[c])

    print("ALTURA MÉDIA DO TIME")
    print(round(soma/12, 2))

    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for i in range(12):
        if altura[i]> (soma/12):
            print(nome[i])
            print('%.2f'% altura[i])
    
if __name__== "__main__":
  main()
