#Exercício 02
#Modelagem de um sistema orientado a objetos: Estacionamento

from veiculo import Veiculo

class Moto(Veiculo): 
  def __init__(self, placa, estacionar): 
    super().__init__(placa, estacionar)
    self._tipo = "Moto"

  def falar_tipo(self):
       print(f"Veículo tipo: {self._tipo}")

Moto = Moto("","")
Moto.falar_tipo()
Moto.estacionar() 

Moto.falar_tipo()
Moto.sair_da_vaga()