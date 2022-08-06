#Exercício 02
#Modelagem de um sistema orientado a objetos: Estacionamento
from veiculo import Veiculo

class Vaga(Veiculo): 
  def __init__(self, id, tipo, livre, placa): 
    self.id = 1 
    self.tipo = "" 
    self.livre = True 
    self.placa = "" 

  def ocupar(self): 
    self.livre = False 
    self.tipo = str(input("Ocupar vaga: Carro ou Moto? "))
    self.placa = input("Placa: ") 
    if self.tipo == "Moto":
      print(f"A moto de placa {self.placa} foi estacionada.\n")
    if self.tipo == "Carro":
      print(f"O carro de placa {self.placa} foi estacionado.\n") 

  def desocupar(self): 
    self.livre = True 
    self.tipo = input("Desocupar vaga: Carro ou Moto? ")
    self.placa = input("Placa: ") 
    if self.tipo == "Moto":
      print(f"A moto de placa{self.placa} saiu da vaga.\n")
    if self.tipo == "Carro":
      print(f"O carro de placa {self.placa} saiu da vaga.\n") 
 
veiculo_01 = Vaga("", "", "", "") 
veiculo_01.ocupar() 
veiculo_01.desocupar() 