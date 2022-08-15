#Definição da classe
class Televisão:
  def __init__(self):
    self.ligada = False
    self.canal = 3
    self.canal_min = 1
    self.canal_max = 99
    self.volume =  30
    self.volume_min = 0
    self.volume_max = 100

    #mudar status
  def ligar(self):
    self.ligada = True

  def desligar(self):
    self.ligada = False

   #mudar canal 
  def mudar_canal_para_cima(self):
    if not self.ligada:
      return
    if self.canal < self.canal_max:
        self.canal += 1

  def mudar_canal_para_baixo(self):
      if not self.ligada:
        return
      if self.canal > self.canal_min:
        self.canal -=1
    
    #mudar volume
  def aumentar_volume (self):
    if not self.ligada:
      return
    if self.volume < self.volume_max:
      self.volume +=10
  def reduzir_volume (self):
    if not self.ligada:
      return
    if self.volume > self.volume_min:
      self.volume -=10

  def __str__(self) -> str:
    return f'\nTelevisão - ligada: {self.ligada} \n- Canal: {self.canal} \n- Volume: {self.volume}'

#Criando instancias da class Televisão
tv_sala =  Televisão()
tv_quarto = Televisão()

#Quando chamamos o método ligar() em uma instância, estamos alterando o estado dela. A outra televisão permanece desligada
tv_sala.ligar()
tv_quarto.ligar()
print('\n#tv_sala está ligada? {}'.format(tv_sala.ligada))
print('#tv_quarto está ligada? {}\n'.format(tv_quarto.ligada))
#print(f'#tv_sala está ligada TESTE? {tv_sala.ligada}') #MESMA SAÍDA

for _ in range(3):
  tv_sala.aumentar_volume()

print('\ntv_sala volume: {}'.format(tv_sala.volume))
print('tv_quarto volume: {}'.format(tv_quarto.volume))

#imprimir o conteúdo do objeto
print('\ntv_sala:', tv_sala)
print('tv_quarto:',tv_quarto)


