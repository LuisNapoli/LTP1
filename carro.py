class Carro:
    def __init__(self, modelo, marca, ano, preco, placa):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.preco = preco
        self.placa = placa

    def get_modelo(self):
        return self.modelo

    def get_marca(self):
        return self.marca

    def get_ano(self):
        return self.ano

    def get_preco(self):
        return self.preco

    def get_placa(self):
        return self.placa

    def get_dados(self):
        return self.modelo, self.marca, self.ano, self.preco, self.placa
