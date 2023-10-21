import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox
import tkinter as tk



class BackEnd:

    # Variáveis de Controle: 
    
    i = 0  # Inicializa a posição na entrada como zero.
    equation = '' # Inicializa a expressão matemática como uma string vazia.

    # Criando metodos para os botôes

    def limpar_c(self):

        # Reniciar a calculadora
        global equation
        self.entrada.delete(0, ctk.END)
        self.equation = ''

        # Reniciar a calculadora
        global equation
        self.entrada.delete(0, ctk.END)
        self.equation = ''

    def backspace(self):

        # Função para limpar os ultimos digitos ao clicar no x
        global equation
        apagando_digito = self.entrada.get()
        apagando_digito = apagando_digito[:-1]  # Remove o último caractere
        self.entrada.delete(0, ctk.END)  # Limpa o campo de entrada
        self.entrada.insert(0, apagando_digito)  # Insere o texto modificado
        self.equation = ''

    def show(self, value):
        if(value=='%'):
            value='/100'

        # Função para aparecer o digito ao clicar no botão
        self.equation += value
        self.entrada.insert(self.i, value)
        self.i = self.i + 1

    def calcular(self):
     # Verifique se a expressão não está vazia
        if not self.equation:
            self.entrada.delete(0, ctk.END)
            self.entrada.insert(0, messagebox.showwarning(title='Calculadora', message='Por favor, insira um valor.'))
            return

        try:
            resultado = eval(self.equation)
            self.entrada.delete(0, ctk.END)
            self.entrada.insert(0, resultado)
        except (ZeroDivisionError, SyntaxError):
            self.entrada.delete(0, ctk.END)
            self.entrada.insert(0, messagebox.showerror(title='Calculadora', message='Não é possivel realizar divisão por zero.'))
        except Exception as e:
             self.entrada.delete(0, ctk.END)
             self.entrada.insert(0, messagebox.showwarning(title='Calculadora', message='Erro desconhecido.'))
      
    def validar_entrada(self, P):
        if all(char in '0123456789+-*/. ' for char in P):
            return True
        return False


class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.interface()
        self.campo_de_entrada()
        self.botoes()

    # Criando interface

    def interface(self):
        self.geometry('330x440')
        self.title('Calculadora')
        self.resizable(False, False)
        set_appearance_mode('light')

        self.protocol("WM_DELETE_WINDOW", self.fechar_janela)

    # Criando campo de entrada de numeros e posicionando

    def campo_de_entrada(self):
        self.entrada = ctk.CTkEntry(
            master=self,
            width=308,
            height=80,
            justify='right',
            border_width=0,
            font=('Arial', 35),
            validate='key',
            validatecommand=(self.register(self.validar_entrada), '%P')
        )
        self.entrada.place(
            x=10,
            y=40
        )

    # Criando botôes dos numeros

    def botoes(self):
        self.resto_divisao = ctk.CTkButton(
            master=self,
            corner_radius=7,
            text='%',
            font=('Arial', 16),
            width=75,
            text_color='black',
            hover_color='#D3D3D3',
            fg_color='#FFF0F5',
            height=50,
            command=lambda: self.show('%')
        )
        self.resto_divisao.place(
            x=10,
            y=155
        )
        self.digito_C = ctk.CTkButton(
            master=self,
            corner_radius=7,
            text='C',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=self.limpar_c
        )
        self.digito_C.place(
            x=166,
            y=155,
        )

        self.digito_apagar = ctk.CTkButton(
            master=self,
            corner_radius=7,
            text='⌫',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=self.backspace,
        )
        self.digito_apagar.place(
            x=88,
            y=155
        )
        self.potencia = ctk.CTkButton(
            master=self,
            corner_radius=7,
            text='**',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('**')
        )
        self.potencia.place(
            x=10,
            y=375
        )
        self.digito_divisao = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='/',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 25),
            width=75,
            height=50,
            command=lambda: self.show('/')
        )
        self.digito_divisao.place(
            x=244,
            y=155
        )
        self.digito_7 = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='7',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('7')
        )
        self.digito_7.place(
            x=10,
            y=210
        )
        self.digito_8 = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='8',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('8')

        )
        self.digito_8.place(
            x=88,
            y=210
        )
        self.digito_9 = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='9',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('9')
        )

        self.digito_9.place(
            x=166,
            y=210
        )
        self.digito_multi = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='*',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 26),
            width=75,
            height=50,
            command=lambda: self.show('*')

        )
        self.digito_multi.place(
            x=244,
            y=210
        )
        self.digito_4 = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='4',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('4')

        )
        self.digito_4.place(
            x=10,
            y=265
        )
        self.digito_5 = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='5',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('5')
        )
        self.digito_5.place(
            x=88,
            y=265
        )
        self.digito_6 = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='6',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('6')
        )
        self.digito_6.place(
            x=166,
            y=265
        )
        self.digito_subtracao = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='-',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 30),
            width=75,
            height=50,
            command=lambda: self.show('-')
        )
        self.digito_subtracao.place(
            x=244,
            y=265
        )
        self.digito_1 = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='1',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('1')
        )
        self.digito_1.place(
            x=10,
            y=320
        )
        self.digito_2 = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='2',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('2')
        )
        self.digito_2.place(
            x=88,
            y=320
        )
        self.digito_3 = ctk.CTkButton(
            master=self,
            text='3',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('3')
        )
        self.digito_3.place(
            x=166,
            y=320
        )
        self.digito_adicao = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='+',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 20),
            width=75,
            height=50,
            command=lambda: self.show('+'),
        )
        self.digito_adicao.place(
            x=244,
            y=320
        )
        self.digito_0 = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='0',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 16),
            width=75,
            height=50,
            command=lambda: self.show('0')
        )
        self.digito_0.place(
            x=88,
            y=375
        )
        self.digito_virgula = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text=',',
            text_color='black',
            fg_color='#FFF0F5',
            hover_color='#D3D3D3',
            font=('Arial', 26),
            width=75,
            height=50,
            command=lambda: self.show(',')
        )
        self.digito_virgula.place(
            x=166,
            y=375
        )
        self.digito_resultado = ctk.CTkButton(
            master=self,
            corner_radius=9,
            text='=',
            text_color='black',
            fg_color='#DEB887',
            hover_color='#F4A460',
            font=('Arial', 16),
            width=75,
            height=50,
            command=self.calcular
        )
        self.digito_resultado.place(
            x=244,
            y=375
        )

    def fechar_janela(self):
        # Função para confirmar o fechamento da janela
        confirmacao = messagebox.askokcancel("Calculadora", "Tem certeza de que deseja sairora?")
        if confirmacao:
            self.destroy()  # Fecha a janela se o usuário confirmar

if __name__ == "__main__":
    app = App()
    app.mainloop()
