#Aula01

#Definição da classe
class Carro:
  def __init__(self):
    self.ligado = False
    self.velocidade = 30
    self.velocidade_min = 0
    self.velocidade_max = 200
    self.cor = 'prata'
    self.modelo = 'uno'
  
  #mudar status
  def ligar(self):
    self.ligado = True

  def desligar(self):
    self.ligado = False

  #mudar velocidade
  def velocidade_acelera(self):
    if not self.ligado:
      return
    if self.velocidade < self.velocidade_max:
        self.velocidade += 10

  def velocidade_desacelera(self):
      if not self.ligado:
        return
      if self.velocidade > self.velocidade_min:
        self.velocidade -=10
    
  def __str__(self) -> str:
    return f'\nCarro: \n- ligado: {self.ligado} \n- velocidade: {self.velocidade}\n'

#Criando instancias da class Carro
carro_01 =  Carro()

#Quando chamamos o método ligar() em uma instância, estamos alterando o estado dela. A outra Carro permanece desligado
carro_01.ligar()
print(f'\n#carro_01 está ligado? {carro_01.ligado}')

for _ in range(10):
  carro_01.velocidade_acelera()
print(f'#carro_01 velocidade: {carro_01.velocidade}.')

#imprimir o conteúdo do objeto
print('\ncarro_01:', carro_01)