# Importando bibliotecas
import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox
import re
from validate_email_address import validate_email


class BackEnd():
    def conecta_db(self):
        self.conn = sqlite3.connect('Sistema_cadastros.db')
        self.cursor = self.conn.cursor()
        print("Banco de dados conectado com sucesso")

    def desconecta_db(self):
        self.conn.close()
        print("Banco de dados desconectado com sucesso")

    def cria_tabela(self):
        self.conecta_db()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuarios(
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Email TEXT NOT NULL,
            Senha TEXT NOT NULL,
            Confirma_Senha TEXT NOT NULL
        );
        ''')
        self.conn.commit()
        print('Tabela Criada com sucesso!')
        self.desconecta_db()

    def cadastrar_usuario(self):
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.senha_cadastro_entry.get()
        self.confirma_senha_cadastro = self.confirmar_senha_entry.get()

        self.conecta_db()

        # Verifica se o nome de usuário já existe
        self.cursor.execute('SELECT * FROM Usuarios WHERE Username = ?', (self.username_cadastro,))
        existing_user = self.cursor.fetchone()

        # Verifica se o e-mail já existe
        self.cursor.execute('SELECT * FROM Usuarios WHERE Email = ?', (self.email_cadastro,))
        existing_email = self.cursor.fetchone()

        def cadastrar_usuario(self):
            self.username_cadastro = self.username_cadastro_entry.get()
            self.email_cadastro = self.email_cadastro_entry.get()
            self.senha_cadastro = self.senha_cadastro_entry.get()
            self.confirma_senha_cadastro = self.confirmar_senha_entry.get()

            self.conecta_db()

        # Formatando primeira letra do nome para maiuscula
        username_cadastro_capitalized = self.username_cadastro.capitalize()

        self.cursor.execute('''
            INSERT INTO Usuarios (Username, Email, Senha, Confirma_Senha)
            VALUES (?, ?, ?, ?)''', (self.username_cadastro, self.email_cadastro, self.senha_cadastro, self.confirma_senha_cadastro))

        try:
            if (self.username_cadastro == "" or self.email_cadastro == "" or self.senha_cadastro == "" or self.confirma_senha_cadastro == ""):
                messagebox.showerror(title='Sistema de Login',
                message="Por favor preencha todos os campos!")
            elif (' ' in self.username_cadastro):
                messagebox.showerror(title="Sistema de Login", message="O usuario não podem ter espaço")
            elif (len(self.username_cadastro) < 4):
                messagebox.showwarning(title='Sistema de Login', message='O nome de usuário deve ter pelo menos 4 caracteres.')
            elif (self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror(title="Sistema de Login", message="As senhas não conferem.")
            elif (len(self.senha_cadastro) < 8):
                messagebox.showwarning(title='Sistema de Login', message='A senha deve conter pelo menos 8 caracteres.')
            elif not re.search(r'[A-Z]', self.senha_cadastro):
                messagebox.showerror(title='Sistema de Login', message='A senha deve conter pelo menos uma letra maiuscula.')
            elif not re.search(r'\d', self.senha_cadastro):
                messagebox.showerror(title='Sistema de Login', message='A senha deve conter pelo menos um numero.')
            elif not re.search(r'[!@#$%^&*()_+]', self.senha_cadastro):
                messagebox.showerror(title='Sistema de Login', message='A senha deve conter pelo menos um caracter especial.')
            elif not validate_email(self.email_cadastro):
                messagebox.showerror(title='Sistema de Login', message='O email não é válido, Por favor digite um email valido.')

            else:
                self.conn.commit()
                messagebox.showinfo(title='Sistema de Login', message=f'Parabens, {username_cadastro_capitalized}!\nOs seus dados foram cadastrados com sucesso!')
                self.desconecta_db()
                self.limpa_entry_cadastro()
        except:
            messagebox.showerror(title='Sistema de Login', message='Erro no processamento do seu cadastro!\nPor favor tente novamente!')
            self.desconecta_db()

    def verifica_login(self):
        self.username_login = self.username_login_entry.get()
        self.senha_login = self.senha_login_entry.get()

        self.conecta_db()

        self.cursor.execute('''SELECT * FROM Usuarios WHERE Username = ?''', (self.username_login,))
        self.verifica_dados = self.cursor.fetchone()

        try:
            if self.verifica_dados is not None:
                if self.senha_login == self.verifica_dados[3]:  # 3 é a posição da senha na consulta
                    messagebox.showinfo(title='Sistema de Login', message=f'Parabéns, {self.username_login}\nLogin feito com sucesso!')
                    self.desconecta_db()
                    self.limpa_entry_login()
                else:
                    messagebox.showerror(title='Sistema de Login', message="Erro!\nSenha incorreta. Por favor, verifique suas credenciais.")
            else:
                messagebox.showerror(title='Sistema de Login', message="Erro!\nNome de usuário não encontrado. Por favor, verifique suas credenciais.")
            self.desconecta_db()
        except Exception as e:
            print(e)
            messagebox.showerror(title='Sistema de Login', message="Erro desconhecido ao verificar o login.")
            self.desconecta_db()


class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inical()
        self.tela_de_login()
        self.cria_tabela()

    # Configurando a janela principal.
    def configuracoes_da_janela_inical(self):
        self.geometry("700x400")
        self.title('Sistema de Login')
        self.resizable(False, False)

    def tela_de_login(self):
        # Trabalhando com as imagens.
        self.iconbitmap("icon.ico")
        self.img = PhotoImage(file='copyright_a9.png', width=512, height=512)
        self.lb_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.lb_img.place(x=50, y=60)

        # Criar o frame do formulario do login.
        self.frame_login = ctk.CTkFrame(
            self,
            width=350,
            height=380,
            corner_radius=10)

        self.frame_login.place(x=360, y=30)

        # Colocando widgets dentro frame - formulario de login.
        self.lb_title = ctk.CTkLabel(
            self.frame_login,
            text='Faça seu Login',
            font=('Roboto', 22))

        self.lb_title.grid(
            row=0,
            column=0,
            padx=10,
            pady=10)

        self.username_login_entry = ctk.CTkEntry(
            self.frame_login,
            width=300,
            placeholder_text='Nome de usuário',
            font=('Roboto', 14),
            corner_radius=10)

        self.username_login_entry.grid(
            row=1,
            column=0,
            padx=10,
            pady=10)

        self.senha_login_entry = ctk.CTkEntry(
            self.frame_login,
            width=300,
            placeholder_text='Senha de usuário',
            show='*',
            font=('Roboto', 14),
            corner_radius=10)

        self.senha_login_entry.grid(
            row=2,
            column=0,
            padx=10,
            pady=10)

        self.ver_senha = ctk.CTkCheckBox(
            self.frame_login,
            text='Clique para ver a senha',
            fg_color="#424c54",
            hover_color="#333333",
            font=('Roboto', 14),
            corner_radius=20)

        self.ver_senha.grid(
            row=3,
            column=0,
            padx=10,
            pady=10)

        self.btn_login = ctk.CTkButton(
            self.frame_login,
            width=300,
            text='Fazer login',
            fg_color="#424c54",
            hover_color='#333333',
            font=('Roboto', 14),
            corner_radius=10,
            command=self.verifica_login)

        self.btn_login.grid(
            row=4,
            column=0,
            padx=10,
            pady=10)

        self.sap = ctk.CTkLabel(
            self.frame_login,
            text='Se não tem conta, clique no botão abaixo para se\n cadastrar no nosso sistema!',
            font=('Roboto', 10))

        self.sap.grid(
            row=5,
            column=0,
            pady=10,
            padx=10)

        self.btn_cadastro = ctk.CTkButton(
            self.frame_login,
            width=300,
            text='Cadastrar-se',
            fg_color="#808080",
            hover_color="#333333",
            font=('Roboto', 14),
            corner_radius=10,
            command=self.tela_De_cadastro)

        self.btn_cadastro.grid(
            row=6,
            column=0,
            padx=10,
            pady=10)

    def tela_De_cadastro(self):
        # Remover o Formularo de Login.
        self.frame_login.place_forget()

        # Criar o frame do formulario do Cadastro.
        self.frame_cadastro = ctk.CTkFrame(
            self,
            width=350,
            height=380,
            corner_radius=10)

        self.frame_cadastro.place(x=360, y=30)

        # Criando o Titulo.
        self.lb_title = ctk.CTkLabel(
            self.frame_cadastro,
            text='Faça seu cadastro',
            font=('Roboto', 22))

        self.lb_title.grid(
            row=0,
            column=0,
            pady=5)

        # Criar widgets da tela de Cadastro.
        self.username_cadastro_entry = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Nome de usuário',
            font=('Roboto', 14),
            corner_radius=10)

        self.username_cadastro_entry.grid(
            row=1,
            column=0,
            padx=10,
            pady=8)

        self.email_cadastro_entry = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Email de usuário',
            font=('Roboto', 14),
            corner_radius=10)

        self.email_cadastro_entry.grid(
            row=2,
            column=0,
            padx=10,
            pady=8)

        self.senha_cadastro_entry = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Senha de usuário',
            font=('Roboto', 14),
            corner_radius=10,
            show='*')

        self.senha_cadastro_entry.grid(
            row=3,
            column=0,
            padx=10,
            pady=8)

        self.confirmar_senha_entry = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Repita sua senha',
            font=('Roboto', 14),
            corner_radius=10,
            show='*')
        self.confirmar_senha_entry.grid(
            row=4,
            column=0,
            padx=10,
            pady=8)

        self.ver_senha = ctk.CTkCheckBox(
            self.frame_cadastro,
            text='Clique para ver a senha',
            fg_color="#424c54",
            hover_color="#333333",
            font=('Roboto', 14),
            corner_radius=20)

        self.ver_senha.grid(row=5, column=0)

        self.btn_cadastrar_user = ctk.CTkButton(
            self.frame_cadastro,
            width=300,
            text='Fazer Cadastro',
            fg_color="#424c54",
            hover_color="#333333",
            font=('Roboto', 14),
            corner_radius=10,
            command=self.cadastrar_usuario)

        self.btn_cadastrar_user.grid(
            row=6,
            column=0,
            padx=10,
            pady=8)

        self.btn_voltar_cadastro = ctk.CTkButton(
            self.frame_cadastro,
            width=300,
            text='Voltar',
            fg_color="#808080",
            hover_color="#333333",
            font=('Roboto', 16),
            corner_radius=10,
            command=self.tela_de_login)

        self.btn_voltar_cadastro.grid(
            row=7,
            column=0,
            padx=10,
            pady=8)

    
    # Limpando as entry de cadastro
    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.senha_cadastro_entry.delete(0, END)
        self.confirmar_senha_entry.delete(0, END)

    # Limpando as entry de login
    def limpa_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.senha_login_entry.delete(0, END)

if __name__ == "__main__":
    app = App()
    app.mainloop()
