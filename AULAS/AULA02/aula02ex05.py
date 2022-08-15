#Em Python, getters e setters não são os mesmos de outras linguagens de programação orientadas a objetos. Basicamente, o principal objetivo do uso de getters e setters em programas orientados a objetos é garantir o encapsulamento dos dados. Variáveis ​​privadas em python não são campos ocultos como em outras linguagens orientadas a objetos. Getters e Setters em python são frequentemente usados ​​quando:

#Usamos getters e setters para adicionar lógica de validação em torno de obter e definir um valor.
# Para evitar o acesso direto de um campo de classe, ou seja, variáveis ​​privadas não podem ser acessadas diretamente ou modificadas por usuários externos.

#Em Python property()é uma função interna que cria e retorna um objeto de propriedade. Um objeto de propriedade tem três métodos, getter(), setter() e delete(). property() função em Python tem quatro argumentos property(fget, fset, fdel, doc), fgeté uma função para recuperar um valor de atributo. fseté uma função para definir um valor de atributo. fdel é uma função para excluir um valor de atributo. doc cria uma docstring para o atributo. Um objeto de propriedade tem três métodos, getter(), setter(), e delete()para especificar fget, fsete fdelindividualmente. Por exemplo

# Python program showing a
# use of property() function
  
# class Geeks:
#      def __init__(self):
#           self._age = 0
       
#      # function to get value of _age
#      def get_age(self):
#          #print("getter method called")
#          return self._age
       
#      # function to set value of _age
#      def set_age(self, a):
#          #print("setter method called")
#          self._age = a
  
#      # function to delete _age attribute
#      def del_age(self):
#          del self._age
     
#      age = property(get_age, set_age, del_age) 
  
# mark = Geeks()
  
# mark.age = 10
  
# print(mark.age)

# Usando decoradores @property para obter o comportamento de getters e setters

# No método anterior, usamos property()a função para obter o comportamento de getters e setters. No entanto, como mencionado anteriormente neste post, getters e setters também são usados ​​para validar a obtenção e configuração do valor dos atributos. Há mais uma maneira de implementar a função de propriedade, ou seja, usando decorator . Python @property é um dos decoradores integrados. O principal objetivo de qualquer decorador é alterar seus métodos ou atributos de classe de forma que o usuário de sua classe não precise fazer nenhuma alteração em seu código. Por exemplo

# Python program showing the use of
# @property

class Geeks:
	def __init__(self):
		self._age = 0
	
	# using property decorator
	# a getter function
	@property
	def age(self):
		print("getter method called")
		return self._age
	
	# a setter function
	@age.setter
	def age(self, a):
		if(a < 18):
			raise ValueError("Sorry you age is below eligibility criteria")
		print("setter method called")
		self._age = a

mark = Geeks()

mark.age = 19

print(mark.age)
