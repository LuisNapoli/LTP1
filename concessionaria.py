import os
from carro import Carro
from vendedor import Vendedor
from comprador import Comprador
from venda import Venda

class Concessionaria:
    def __init__(self):
        self.carros = []
        self.comprador = []
        self.vendedor = []
        self.venda = []
        self.vendas = []
    def text_carros(self):
        if os.path.exists('Carros.txt'):
            file = open('Carros.txt', 'r')
            for c in file.readlines():
                c = c.strip().lstrip('(').rstrip(')').split(',')
                carro = Carro(c[0].strip().strip('"').strip("'"),
                              c[1].strip().strip('"').strip("'"),
                              c[2].strip().strip('"').strip("'"),
                              float(c[3].strip().strip('"').strip("'")),
                              c[4].strip().strip('"').strip("'"))
                self.carros.append(carro)
        else:
            file = open('Carros.txt', 'w')
        file.close()
    def text_vendas(self):
        if os.path.exists('Vendas.txt'):
            file = open('Vendas.txt', 'r')
            for c in file.readlines():
                c = c.strip().lstrip('((').rstrip(')').split(',')
                carro = Carro(c[0].strip().strip('"').strip("'"),
                              c[1].strip().strip('"').strip("'"),
                              c[2].strip().strip('"').strip("'"),
                              float(c[3].strip().strip('"').strip("'")),
                              c[4].strip().strip('),').strip("'").strip('"'))

                venda = Vendedor(c[5].strip().strip('(').strip('"').strip("'"),
                                c[6].strip().strip('),').strip("'").strip('"'))

                compra = Comprador(c[7].strip().strip('(').strip('"').strip("'"),
                                 c[8].strip().strip('),').strip("'").strip('"'))

                preco = float(c[9])

                venda = Venda(carro, venda, compra, preco)

                self.vendas.append(venda)
        else:
            file = open('Vendas.txt', 'w')
        file.close()

    def text_compradores(self):
        if os.path.exists('Compradores.txt'):
            file = open('Compradores.txt', 'r')
            for c in file.readlines():
                c = c.strip().lstrip('(').rstrip(')').split(',')
                compra = Comprador(c[0].strip().strip('"').strip("'"),
                                     c[1].strip().strip('"').strip("'"))
                self.comprador.append(compra)
        else:
            file = open('Compradores.txt', 'w')
        file.close()
    def text_vendedores(self):
        if os.path.exists('Vendedores.txt'):
            file = open('Vendedores.txt', 'r')
            for c in file.readlines():
                c = c.strip().lstrip('(').rstrip(')').split(',')
                venda = Vendedor(c[0].strip().strip('"').strip("'"),
                                c[1].strip().strip('"').strip("'"))
                self.vendedor.append(venda)
        else:
            file = open('Vendedores.txt', 'w')
        file.close()

    def text_vendas(self):
        if os.path.exists('Vendas.txt'):
            file = open('Vendas.txt', 'r')
            for c in file.readlines():
                c = c.strip().lstrip('(').rstrip(')').split(',')
                carro = Carro(c[0].strip().strip('"').strip("'"),
                              c[1].strip().strip('"').strip("'"),
                              c[2].strip().strip('"').strip("'"),
                              float(c[3].strip().strip('"').strip("'")),
                              c[4].strip().strip('"').strip("'"))

                venda = Vendedor(c[5].strip().strip('"').strip("'"),
                                c[6].strip().strip('"').strip("'"))

                compra = Comprador(c[7].strip().strip('"').strip("'"),
                                 c[8].strip().strip('"').strip("'"))

                preco = float(c[9])

                venda = Venda(carro, venda, compra, preco)

                self.vendas.append(venda)
        else:
            file = open('Vendas.txt', 'w')
        file.close()

    def adc_carro(self, carro):
        self.carros.append(carro)

    def adc_vendedor(self, vendedor):
        self.vendedor.append(vendedor)

    def adc_comprador(self, comprador):
        self.comprador.append(comprador)
    def adc_venda(self, venda):
        self.venda.append(venda)

    def salv_carro(self):
        file = open('Carros.txt', 'w')
        for c in self.carros:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()
    def salv_comprador(self):
        file = open('Compradores.txt', 'w')
        for c in self.comprador:
            file.write(str(c.get_dados()))
            file.write('\n')
    def salv_vendedor(self):
        file = open('Vendedores.txt', 'w')
        for c in self.vendedor:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()
    def salv_vendas(self):
        file = open('Vendas.txt', 'w')
        for c in self.vendas:
            file.write(str(c.info_venda()))
            file.write('\n')
        file.close()

    def show_carros(self):
        return self.carros
    def show_comp(self):
        return self.comprador
    def show_vend(self):
        return self.vendedor
    def show_vendas(self):
        return self.vendas()

    def show_u_venda(self):
        return self.vendas[len(self.show_vendas()) - 1]

    def remove_car(self, c):
        rmv = c
        self.carros.remove(c)
        return rmv
    def remove_comp(self, c):
        rmv = c
        self.comprador.remove(c)
        return rmv
    def remove_vend(self, v):
        rmv = v
        self.vendedor.remove(v)
        return rmv



