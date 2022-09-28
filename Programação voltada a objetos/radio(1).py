estações = {89.5:'Cocais', 91.5:'Mix', 94.1: 'Boa', 99.1:'Clube'}
i= 0

class RadioFM:
  def __init__ (self, vol_max, estações):
    self.__volume_min=0
    self.volume_max=vol_max
    self.__freq_min = 88
    self.__freq_max= 108
    self.estações= estações
    self.__volume= None
    self.__ligado = False
    self.estação_atual = None
    self.frequencia_atual = None
    self.__antena_habilitada = False

  
  def ligar(self):
    if self.__ligado == False:
      self.ligado = True
      self.volume= self.__volume_min
      self.__antena_habilitada = True
      self.frequencia_atual = 89.5
      self.estação_atual = estações[89.5]
    else:
      print("O rádio já está ligado.")
    
    
  def desligar(self):
    if self.__ligado == True:
      self.__ligado = False
      self.__volume= None
      self.__antena_habilitada = False
      self.frequencia_atual = None
      self.estação_atual = None
    else:
      print("O rádio já está desligado.")

    
  def aumentar_volume(self, vol):
    while vol<1:
      vol= int(input("O valor digitado não pode ser menor que 1: "))
    
    if vol == None:
      self.__volume+= 1 
    
    if vol >1:
      self.__volume= vol
    
    if self.__volume > self.volume_max:
      self.__volume = self.volume_max
    print(self.__volume)
    
  def diminuir_volume(self,vol):
    while vol< 1:
      vol= int(input("O valor digitado não pode ser menor que 1: "))
    
    if vol == None:
      self.__volume-= 1 
    
    if vol > 1:
      self.__volume= vol
    
    if self.__volume < self.__volume_min:
      self.__volume = self.__volume_min
    print(self.volume)
    
  def mudar_frequencia(self, freq):
    if freq in estações:
      self.frequencia_atual = freq
      self.estação_atual = estações[freq]
    else:
      print("Estação não encontrada.")


r1= RadioFM(50, 91.5)
r1.ligar()
print(r1.ligado)
print(r1.estação_atual)
r1.aumentar_volume(15)
r1.mudar_frequencia( 99.1)
print(r1.frequencia_atual)
print("\n")


r2= RadioFM(33, None)
r2.ligar()
print(r2.ligado)
print(r2.estação_atual)
r2.diminuir_volume(15)
r2.mudar_frequencia( 99.1)
print(r2.frequencia_atual)
r2.desligar()
print("\n")


r3= RadioFM(12, None)
r3.ligar()
print(r3.ligado)
print(r3.estação_atual)
r3.aumentar_volume(15)
r3.mudar_frequencia( 99.1)
print(r3.frequencia_atual)
