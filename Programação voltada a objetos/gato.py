import random
gatos =[]
filhotes= []

sexo_v=["M","F"]
class Gato:
  raça = None
  nome = None
  peso = None
  idade = None
  sexo = None
  fertil = None
  cio = None
  prenhe = None
  puerperio = None

  def mudar_nome(self, nome):
    self.nome = nome
    print(f'Nome do gato mudado para {self.nome}')

  def engordar(self, peso):
    self.peso += peso
    print(f'{self.nome} engordou {peso}kg, seu peso agora é de {self.peso}kg')
  
  def envelhecer(self):
    self.idade += 1
    if self.idade >=1:
      self.fertil=True
    print(f'{self.nome} envelheceu mais 1 ano, idade atual: {self.idade} anos')
  
  def entrar_no_cio(self):
    if self.sexo == 'F' and self.fertil==True and self.prenhe==False and self.puerperio==False:
      self.cio = True
      print(f'{self.nome} entrou no cio')
    else:
      print('Não foi possivel entrar no cio!')
  
  def parir(self):
    quant = random.randint(1,7)

    if self.sexo == 'F' and self.prenhe == True:
      self.puerperio = True
      self.prenhe = False
      self.cio = False
      #colocar um for 
      g = Gato()
      g.sexo=random.choice(sexo_v)
      #incluir na lista
      gatos.append(g)
      filhotes.append(g)
      print("parto realizado com sucesso!")
      return g
      
    else:
      return('Erro!')
  
  def cruzar(self, gato):
       if self.sexo in ["F","M"] and gato.sexo!=self.sexo:
           if self.sexo=="F" and self.fertil==True and self.cio==True and self.puerperio==False and self.prenhe==False and gato.sexo=="M" and gato.fertil==True:
              print("cruzamento realizado com sucesso!")
              self.prenhe==True
              self.cio=False
           elif self.sexo=="M" and self.fertil==True and gato.fertil==True and gato.cio==True and gato.puerperio==False and gato.prenhe==False:
              print("Cruzamento realizado com sucesso!")
              gato.prenhe=True
              gato.cio=False
           else:
             print("Cruzamento não realizado!")

       else:
          print("Erro ao cruzar!")