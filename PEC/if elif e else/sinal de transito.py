print(''' Digite uma cor para o sinal de transito:
V - para verde
A - para amarelo
E - para vermelho''')
x = input().upper()

if x == "V" or x=="VERDE":
    print("Siga em frente.")

elif x == "A" or x=="AMARELO":
    print ("Atenção.")

elif x == "E" or x=="VERMELHO":
    print("Pare.")

else:
    print("Digite V, A ou E.")
