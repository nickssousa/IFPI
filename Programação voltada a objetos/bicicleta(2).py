class Bicicleta():

    def __init__(self, peso, altura, cor, aro, veloc_atual= 0, altura_cela= 0, calibragem_pneus= 20):
      self.peso= peso
      self.altura = altura
      self.cor = cor
      self.aro= aro
      self.altura_cela= altura_cela
      self.calibragem_pneus= calibragem_pneus
      self.veloc_atual= veloc_atual
      self.__calibragemmax= 28
      self.__segundosmax= 60
      self.__alturamax= 8
      self.__alturamin= 0

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


#bicicleta 1:
            
b1= Bicicleta(30, 1.2, "Azul", 20)
print("Bicicleta 1:")
print("Peso:", b1.peso, "kg")
print("Altura:", b1.altura, "m")
print("Cor:", b1.cor)
print("Aro:", b1.aro, "pol")
print("Velocidade atual:", b1.veloc_atual, "km/h")
print("Altura da cela:", b1.altura_cela)
print("Calibragem dos pneus:", b1.calibragem_pneus, "psi\n")

#bicicleta 2:

b2= Bicicleta(20, 1.25, "Verde", 18, 15, 4)
print("Bicicleta 2:")
print("Peso:", b2.peso, "kg")
print("Altura:", b2.altura, "m")
print("Cor:", b2.cor)
print("Aro:", b2.aro, "pol")
print("Velocidade atual:", b2.veloc_atual, "km/h")
print("Altura da cela:", b2.altura_cela)
print("Calibragem dos pneus:", b2.calibragem_pneus,"psi\n")

#bicicleta 3:

b3= Bicicleta(33, 1.4, "Amarelo", 19, 22, 3, 13)
print("Bicicleta 3:")
print("Peso:", b3.peso, "kg")
print("Altura:", b3.altura, "m")
print("Cor:", b3.cor)
print("Aro:", b3.aro, "pol")
print("Velocidade atual:", b3.veloc_atual, "km/h")
print("Altura da cela:", b3.altura_cela)
print("Calibragem dos pneus:", b3.calibragem_pneus, "psi\n")

#bicicleta 4:

b4= Bicicleta(27, 1.35, "Cinza", 20, 12, 6, 24)
print("Bicicleta 4:")
print("Peso:", b4.peso, "kg")
print("Altura:", b4.altura, "m")
print("Cor:", b4.cor)
print("Aro:", b4.aro, "pol")
print("Velocidade atual:", b4.veloc_atual, "km/h")
print("Altura da cela:", b4.altura_cela)
print("Calibragem dos pneus:", b4.calibragem_pneus, "psi\n")
