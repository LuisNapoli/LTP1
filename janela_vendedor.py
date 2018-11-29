from tkinter import *
from vendedor import Vendedor
from tkinter import messagebox


class Janela_vendedor(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)

        self.control = control
        self.title('Vendedor')
        self.geometry('550x400+200+200')
        self.transient(parent)
        self.grab_set()
        Label(self, text='Acrescente um novo Vendedor').grid(row=0, column=2, padx=10, pady=10, stick=N)
        Label(self, text='').grid(row=0, column=0, padx=40, pady=10)
        Label(self, text='Remova um vendedor',fg='red').grid(row=5, column=2, padx=10, pady=20)

        self.btn_add = Button(self, text='Adicionar Vendedor', command=self.adc_vend).\
            grid(row=4, column=1, columnspan=3, pady=10, stick=S)
        self.bt_rmv = Button(self, text='Remover Vendedor',fg='red', command=self.remove_vend).\
            grid(row=9, column=1, columnspan=3, pady=10, stick=S)
        self.btn_close = Button(self, text='Atualizar', command=self.destroy, width=10)
        self.btn_close.grid(row=10, column=1, columnspan=3, stick=S, pady=20)

        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var).\
            grid(row=1, column=3, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome').\
            grid(row=1, column=1, padx=1, pady=1)


        self.entry_mat_var = StringVar()
        self.entry_mat = Entry(self, textvariable=self.entry_mat_var).\
            grid(row=3, column=3, padx=1, pady=1)
        self.lbl_mat = Label(self, text='Matrícula').\
            grid(row=3, column=1, padx=1, pady=1)

        self.entry_mat_var2 = StringVar()
        self.entry_mat2 = Entry(self, textvariable=self.entry_mat_var2). \
            grid(row=6, column=3, padx=1, pady=1)
        self.lbl_mat2 = Label(self, text='Matrícula',fg='red'). \
            grid(row=6, column=1, padx=1, pady=1)


    def adc_vend(self):
        nome = self.entry_nome_var.get()
        matricula = self.entry_mat_var.get()
        v = Vendedor(nome, matricula)
        self.control.bd.adc_vendedor(v)
        messagebox.showinfo('Vendedor', f'{nome} foi adicionado.')

    def remove_vend(self):
        matricula = self.entry_mat_var2.get()
        rmvd = None
        for vend in self.control.bd.show_vend():
            if matricula == vend.get_matricula():
                if messagebox.askyesno\
                            ('Excluir', f'Tem ceteza que deseja excluir o vendedor {vend.get_nome()}?') is False:
                    return None
                rmvd = self.control.bd.remove_vend(vend)
                messagebox.showinfo('Vendedor', f'{vend.get_nome()} foi removido.')
        if rmvd is None:
            messagebox.showerror('Vendedor', 'Não há vendedor cadastrado com esta matrícula')

    def destroy(self):
        self.control.bd.salv_vendedor()
        super().destroy()



