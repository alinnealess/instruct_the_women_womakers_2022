# Exercício 02
# Modelagem de um sistema orientado a objetos: Estacionamento
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, placa, estacionado):
        super().__init__(placa, estacionado)
        self._tipo = "Carro"

    def falar_tipo(self):
        print(f"Veículo tipo: {self._tipo}")

carro = Carro("", "")
carro.falar_tipo()
carro.estacionar()
carro.falar_tipo()
carro.sair_da_vaga()