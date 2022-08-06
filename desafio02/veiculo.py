#Exercício 02
#Modelagem de um sistema orientado a objetos: Estacionamento
class Veiculo(): 
  def __init__(self, placa, estacionado): 
    self.placa = "" 
    self.estacionado = True
    self.tipo = ""
    

  def estacionar(self):
    self.estacionado = True
    print("Ação: Estacionar")
    self.placa = input("Placa: ") 
    print(f"O veículo que possui placa {self.placa} estacionou.\n")

  def sair_da_vaga(self):
    self.estacionado = False
    print("Ação: Sair da vaga") 
    self.placa = input("Placa: ") 
    print(f"O veículo que possui placa {self.placa} saiu da vaga.\n") 