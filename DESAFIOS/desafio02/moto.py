#Exercício 02
#Modelagem de um sistema orientado a objetos: Estacionamento
from veiculo import Veiculo

class Moto(Veiculo): 
  def __init__(self, placa, estacionar): 
    super().__init__(placa, estacionar)
    self._tipo = "Moto"

  def falar_tipo(self):
       print(f"Veículo tipo: {self._tipo}")

moto = Moto("","")
moto.falar_tipo()
moto.estacionar() 
moto.falar_tipo()
moto.sair_da_vaga()