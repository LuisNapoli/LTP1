class Vendedor:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def get_nome(self):
        return self.nome

    def get_matricula(self):
        return self.matricula

    def get_dados(self):
        return self.nome, self.matricula
