from janela_principal import Janela_principal
from concessionaria import Concessionaria



class Controle:
    def __init__(self):
        self.bd = Concessionaria()
        self.bd.text_carros()
        self.bd.text_compradores()
        self.bd.text_vendedores()
        self.bd.text_vendas()
        self.jn = Janela_principal(self)
        self.jn.mainloop()
