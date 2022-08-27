class Bicicleta():

    def __init__(self, altura_cela, calibragem_pneus):
      self.alturamax= 8
      self.alturamin= 3
      self.altura_cela= altura_cela
      self.calibragem_pneus= calibragem_pneus
      self.calibragemmax= 28
      self.segundosmax= 60
      self.veloc_atual= 0


    def acelerar(self, veloc):
        self.veloc_atual+= veloc
        print(f'A sua velocidade atual é de {self.veloc_atual} km/hr.')

    def frear(self, velo):
        if self.veloc_atual > velo:
            self.veloc_atual-= velo
            print(f'A sua velocidade atual é de {self.veloc_atual} km/hr.')

        else:
            self.veloc_atual= 0
            print("Você está parado.")
    
    def calibrar_pneus(self, calibrar):
        if self.veloc_atual ==0:
            self.calibragem_pneus+= calibrar

            if self.calibragem_pneus > self.calibragemmax:
                print("Seu pneu estourou, parabéns.")

            elif self.calibragem_pneus<= 0:
                self.calibragem_pneus= 0
                print("Seu pneu está seco.")
        
            else:
                print(f'Seu pneu agora está com {self.calibragem_pneus} psi.')

        else:
            print("Ação não pode ser executada por que a bicicleta está em movimento.")

    def ajustar_cela(self, altura):
        if self.veloc_atual == 0:
            if altura>0:
                self.altura_cela+= altura
                if self.altura_cela> 8:
                    self.altura_cela = 8

                print(f'A altura da cela foi ajustada para {self.altura_cela}')
        
            elif altura< 0:
                self.altura_cela+= altura
                if self.altura_cela< 3:
                    self.altura_cela = 3

                print(f'A altura da cela foi ajustada para {self.altura_cela}')
        
        else:
            print("Ação não pode ser executada por que a bicicleta está em movimento.")




#bicicleta:
            
b1= Bicicleta(5, 15)
b1.acelerar(13)
b1.acelerar(10)
b1.frear(30)
b1.calibrar_pneus(-50)
b1.calibrar_pneus(20)
b1.ajustar_cela(10)
b1.ajustar_cela(-2)

