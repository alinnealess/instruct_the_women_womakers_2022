# herança

class Pessoa:
    def __init__(self, nome):
        self._nome = nome
        self._tipo = 'Pessoa'

    def falar_oi(self):
        print('Oi, meu nome é {}.'.format(self._nome))

    def falar_tipo(self):
        print('Oi, meu tipo é {}.'.format(self._tipo))


# pessoa = Pessoa('Maria')
# pessoa.falar_oi()
# pessoa.falar_tipo()

#a classe estudante é derivada da classe Pessoa
#relação: estudante é uma pessoa

class Estudante(Pessoa):
  def __init__(self, nome, curso):
      super().__init__(nome) #chama o construtor na classe base
      self._curso = curso
  
  def falar_curso(self):
    print(f'Eu, {self._nome}, estudo o curso {self._curso}.')
    #a propriedade self._nome é herdada da calsse base

  def falar_tipo(self):
    self._tipo = 'Estudante'
    return super().falar_tipo()
    
estudante = Estudante('Yasmin', 'Introdução ao Python')
estudante.falar_oi() # o método "falar_oi" é herdado da classe base
estudante.falar_tipo() #o método "falar_tipo" é herdado da classe base, e sobreescrito na classe derivada
estudante.falar_curso()
