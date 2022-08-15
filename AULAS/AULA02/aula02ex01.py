# Encapsulamento
class Pessoa:
    def __init__(self, nome, profissao, identidade):
        self._nome = nome  # dado sensivel
        self.profissao = profissao
        self.__identidade = identidade  # dado sensivel

    def __str__(self):
        return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self.__identidade}'

pessoa1 = Pessoa('Ana', 'Programadora', '123456')
print(pessoa1)

#ao tentar alterar um atributo publico, o valor é alterado
pessoa1.profissao = 'Médica'
print(pessoa1)

#ao tentar alterar um atributo privado, o valor não é alterado
pessoa1.__identidade = '2359595'
print(pessoa1)

#ao tentar alterar um atributo protegido, vamos conseguir 
pessoa1._nome = 'Marta'
print(pessoa1)