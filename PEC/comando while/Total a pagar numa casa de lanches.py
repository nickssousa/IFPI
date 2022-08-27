def main():
    conta= 0
    while True:
        print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
        a= input().lower().strip()
        if a== 'h':
            conta+= 5.50
        if a== 'c':
            conta+= 6.80
        if a== 'm':
            conta+= 4.50
        if a== 'a':
            conta+= 7.00
        if a== 'q':
            conta+= 4.00
        if a== 'x':
            break
    print("%.2f"%conta)
        

if __name__== "__main__":
  main()

