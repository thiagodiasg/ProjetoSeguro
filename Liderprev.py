from funções import *
from tkinter import*
import sqlite3


def MarcasCarro():
    print("Bt click")
    bt1 = Button(janela, width=20, text="Fiat")
    bt2 = Button(janela, width=20, text="Chevrolet")
    bt3 = Button(janela, width=20, text="Toyota")
    bt4 = Button(janela, width=20, text="Jeep")
    bt5 = Button(janela, width=20, text="Ford")
    bt6 = Button(janela, width=20, text="Honda")
    bt7 = Button(janela, width=20, text="Volkswagem")
    bt8 = Button(janela, width=20, text="Nissan")
    bt9 = Button(janela, width=20, text="Mitsubish")
    bt10 = Button(janela, width=20, text="Hyundai")
    bt11 = Button(janela, width=15, text="Voltar", command = inicial)
    bt1.place(x=25, y=20)
    bt2.place(x=25, y=60)
    bt3.place(x=25, y=100)
    bt4.place(x=25, y=140)
    bt5.place(x=25, y=180)
    bt6.place(x=25, y=220)
    bt7.place(x=25, y=260)
    bt8.place(x=25, y=300)
    bt9.place(x=25, y=340)
    bt10.place(x=25, y=380)
    bt11.place(x=40, y=420)
    janela.geometry("300x480+200+200")


def inicial():
    global janela
    janela.destroy()
    janela = Tk()
    janela['bg'] = "black"
    bt1 = Button(janela, width=20, text="Linha Leve",font="MalgunGothic 9 bold",bg = 'white' ,command= MarcasCarro)
    bt2 = Button(janela, width=20, text="Linha Pesada",font="MalgunGothic 9 bold",bg = 'white', command=MarcasCarro)
    bt3 = Button(janela, width=20, text="Motocicletas",font="MalgunGothic 9 bold",bg = 'white', command=MarcasCarro)
    bt4 = Button(janela, width=15, text="Log out",font="MalgunGothic 9 bold",bg = 'white', command = Escolha)
    bt1.place(x=25, y=20)
    bt2.place(x=25, y=60)
    bt3.place(x=25, y=100)
    bt4.place(x=40, y=140)
    janela.geometry("190x190+500+200")

def Escolha():
    global janela
    janela.destroy()
    janela = Tk()
    janela['bg'] = 'black'
    bt1 = Button(janela, width=20, text="Login",font = "MalgunGothic 9 bold",bg = 'white', command=logindados)
    bt2 = Button(janela, width=20, text="Cadastrar-se",font = "MalgunGothic 9 bold",bg = 'white', command=inicial)
    bt3 = Button(janela, width=20, text="Desenvolvedores",font = "MalgunGothic 9 bold",bg = 'white' ,command=Desenvolvedores)
    bt1.place(x=25,y=20)
    bt2.place(x=25, y=60)
    bt3.place(x=25, y=100)

    janela.geometry("190x190+500+200")

def logindados():
    global janela
    janela.destroy()
    janela = Tk()
    entrada1 = Entry(janela,width = 15)
    entrada2 = Entry(janela, width = 15)
    lb1 = Label(janela,text = "Login: ")
    lb2 = Label(janela,text="Senha: ")
    btlogin = Button(janela, width =15 , text = "Logar", command = inicial)
    lb1.place(x = 25 , y = 60)
    lb2.place(x = 22, y = 90)
    entrada1.place(x=70,y = 60)
    entrada2.place(x=70,y=90)
    btlogin.place(x=50,y = 120)
    janela.geometry("190x190+500+200")
def Desenvolvedores():
    global janela
    janela.destroy()
    janela = Tk()
    lb90 = Label(janela, text = "Este programa foi desevolvido para finalidades\n educacionais, Desevolvido por um grupo de aluno \nda UEPB, para um projeto de Algoritmos", )
    lb90.place(x=10, y=120)
    bt4 = Button(janela, width=15, text="Voltar", command = Voltar)
    bt4.place(x=40, y=190)

    janela.geometry("300x300+200+200")
def Voltar():
    global janela
    janela.destroy()
    janela = Tk()
    Escolha()

global janela
janela = Tk()


Escolha()

janela.mainloop()

'''from tkinter import *
import sqlite3


def banco():

    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()
    # criando a tabela (schema)
    cursor.execute("""
CREATE TABLE usuario (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf     VARCHAR(11) NOT NULL,
        user VARCHAR(10),
        senha VARCHAR(10)
);
""")

    print('Tabela criada com sucesso.')
    conexao.close()


def login():
    verificaSenha = 000
    verificaUser = 'Nulo'
    usuario = caixaUser.get()
    senha = caixaSenha.get()
    # recebe na entrada usuario e senha

    # Conectando o BANCO liderPrev
    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()

    # VERIFICANDO SE A SENHA ESTÁ DENTRO DO BANCO

    cursor.execute("""
SELECT senha FROM usuario
WHERE user = ?
""", (usuario,))

    x = cursor.fetchall()
    if len(x) > 0:
        verificaSenha = x[0][0]

    cursor.execute("""
  SELECT user FROM usuario
  WHERE user = ?
  """, (usuario,))

    x = cursor.fetchall()
    if len(x) > 0:
        verificaUser = x[0][0]

    if senha == verificaSenha and verificaUser == usuario:
        print("senha Correta")
    else:
        print("senha e/ou usuario incorreto")


def cadastro():
    janela2 = Tk()
    janela2.title("Cadastro Usuario")
    janela2.geometry("600x600+150+150")

    conn = sqlite3.connect('liderPrev.db')
    cursor = conn.cursor()

    labelNomeCompleto = Label(janela2, text="Nome Completo:")
    labelNomeCompleto.pack()
    caixaNomeCompleto = Entry(janela2)
    caixaNomeCompleto.pack()
    # nome = str(input("{:s}".format("Nome Completo: ",end="")))
    labelUser = Label(janela2, text="Usuario:")
    labelUser.pack()
    caixaUser = Entry(janela2)
    caixaUser.pack()
    # usuario = str(input("{:s}".format("USUÁRIO: ",end="")))
    labelSenha = Label(janela2, text="Senha:")
    labelSenha.pack()
    caixaSenha = Entry(janela2)
    caixaSenha.pack()
    # senha = getpass.getpass("SENHA: ")
    labelCpf = Label(janela2, text="CPF:")
    labelCpf.pack()
    caixaCpf = Entry(janela2)
    caixaCpf.pack()

    # cpf = str(input("{:s}".format("CPF: ",end="")))
    # CAIO gAY

def inserir():
    cursor.execute("""INSERT INTO usuario (nome, cpf, user, senha) VALUES (?, ?, ?, ?)""",
                       (caixaNomeCompleto.get(), caixaCpf.get(), caixaUser.get(), caixaSenha.get()))

    butao = Button(janela2, text="Cadastrar")
    butao.pack()
    butao["command"] = inserir

    janela2.mainloop()
    # inserindo dados na tabela

    # gravando no bd

    conn.commit()

    print('Usuario cadastrado com sucesso!! ')

    conn.close()


    janela = Tk()
    janela.title("LiderPrev 1.0 ")

    labelUser = Label(janela, text="Usuario:")
    labelUser.pack()

    caixaUser = Entry(janela)
    caixaUser.pack()

    labelSenha = Label(janela, text="Senha:")
    labelSenha.pack()

    caixaSenha = Entry(janela)
    caixaSenha.pack()

    butaoEntrar = Button(janela, text="Entrar")
    butaoEntrar["command"] = login
    butaoEntrar.pack()

    labelSemCad = Label(janela, text="Não tem cadastro?")
    labelSemCad.pack()

    butaoCadastrar = Button(janela, text="Cadastrar-se")
    butaoCadastrar["command"] = cadastro
    butaoCadastrar.pack()

    janela.geometry("200x200+100+100")

    janela.mainloop()

    conexao = sqlite3.connect("liderPrev.db")
    cursor = conexao.cursor()

# for i in range(20):
#    cursor.execute("DELETE FROM usuario WHERE id = ?",(i,))

    cursor.execute("SELECT * FROM usuario")

    for i in cursor.fetchall():
        print(i)
'''