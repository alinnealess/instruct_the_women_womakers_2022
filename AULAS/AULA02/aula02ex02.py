#getter = retorna valor
#setter = definir ou atualizar

class Quadrado:
  def __init__(self, medida):
    self.altura= medida
    self.largura = medida
  
  @property
  def altura(self):
    print('Getter de altura')
    return self.__medida

  @altura.setter
  def altura(self, valor):
    print('Setter altura')

    if (valor <0):
      raise ValueError()
    self.__medida = valor
  
  @property
  def largura(self):
    print('Getter de largura')
    return self.__medida

  @largura.setter
  def largura(self, valor):
    print('setter de largura')
    if (valor <0):
      raise ValueError()
    self.__medida = valor

  def area(self):
    return self.largura * self.altura

quadrado = Quadrado(2)
print(quadrado.area())
quadrado.altura = 3
print(quadrado.area())
quadrado.largura = 4
print(quadrado.area())
