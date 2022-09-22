quant_questoes= 30
gabarito= []
respostas= []

def receber_gabarito():
  print("\n****** Digite o gabarito oficial da prova*******")
  for i in range(quant_questoes):
    while True:
      resposta= input("\nQuestão %d: "%(i + 1)).upper()
      if resposta in("A","B","C","D","E"):
        gabarito.append(resposta)
        break
      
      else:
        print("Alternativa inválida. Digite apenas A, B, C, D, E.")
  print("Gabarito oficial: ", gabarito)

def receber_respostas_alunos():
  n_alunos = int(input("\nDigite o número de alunos da turma: "))
  for i in range(n_alunos):
    numero_do_aluno = int(input("\nDigite o número do(a) %d aluno(a): "% (i+1)))
    acertos = 0
    respostas= list(range(quant_questoes))
    for j in range(quant_questoes):
      while True:
        resposta = input("\nDigite a resposta da questão %d: "%(j+1)).upper()
        if resposta in ("A","B","C","D","E"):
          respostas[j]= resposta
          break
        else:
          print("Resposta inválida. Digite apenas A,B,C,D,E.")
      
      if respostas[j] == gabarito[j]:
        acertos += 1
    print("\n", gabarito)
    print("\n", respostas)
    print("O aluno de número %d teve %d acerto(s)."% (numero_do_aluno, acertos))

receber_gabarito()
receber_respostas_alunos()
