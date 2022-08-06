# Exercício 02
# Modelagem de um sistema orientado a objetos: Estacionamento
class Estacionamento():
    def __init__(self, vagas_de_carro, vagas_de_moto, carro_para_vaga, moto_para_vaga, total_vagas_livres_carro, total_vagas_livres_moto):
        self.vagas_de_carro = 25
        self.vagas_de_moto = 25
        self.carro_para_vaga = 3
        self.moto_para_vaga = 2
        self.total_vagas_livres_carro = 25
        self.total_vagas_livres_moto = 25

    def estacionar_carro(self):
        self.total_vagas_livres_carro -= 1
        
    def estacionar_moto(self):
        self.total_vagas_livres_moto -= 1

    def remover_carro(self):
        self.total_vagas_livres_carro += 1

    def remover_moto(self):
        self.total_vagas_livres_moto += 1

    def estado_do_estacionamento(self):
        if self.total_vagas_livres_carro == 0:
            print(f"Status Estacionamento Carro:")
            print(f"Não há vagas para carros.\n")
        else:
            print(f"Status Estacionamento Carro:")
            print(f"{self.total_vagas_livres_carro} vagas de carro livres.\n")

        if self.total_vagas_livres_moto == 0:
            print(f"Status Estacionamento Moto:")
            print(f"Não há vagas para motos\n")
        else:
            print(f"Status Estacionamento Moto:")
            print(f"{self.total_vagas_livres_moto} vagas de moto livres.\n")

situacao = Estacionamento("", "", "", "", "", "")
situacao.estacionar_carro()
situacao.estacionar_moto()
situacao.estado_do_estacionamento()
situacao.remover_carro()
situacao.remover_moto()
situacao.estado_do_estacionamento()