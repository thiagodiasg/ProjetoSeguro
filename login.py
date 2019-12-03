from tkinter import *
from banco import *
from Frames import *
import Frames

def telaLogin(janela):
    janela.destroy()
    janela = Tk()
    janela.iconbitmap('imagesico (2).ico')
    janela.title("Lider Prev - v3.7")
    janela.geometry('300x300+500+100')
    janela.resizable(0, 0)
    janela['bg'] = '#03467B'
    janela.iconbitmap('imagesico (2).ico')
    janela['bg'] = '#03467B'
    janela.resizable(0, 0)
    janela.geometry('300x300+500+100')
    labelUser = Label(janela, text="Usuario:",foreground="white", bg="#03467B", font="Helvetica 9 bold")
    labelUser.pack()

    caixaUser = Entry(janela, bg='white', fg='black', font="Helvetica 9 bold")
    caixaUser.pack()

    labelSenha = Label(janela, text="Senha:", foreground="white", bg="#03467B", font="Helvetica 9 bold")
    labelSenha.pack()

    caixaSenha = Entry(janela, bg='white', fg='black', font="Helvetica 9 bold",show = '*')
    caixaSenha.pack()


    butaoEntrar = Button(janela, text="Entrar", font="Helvetica 9 bold", bg='white',command=lambda : auxiliar(caixaUser.get(),caixaSenha.get(),janela))
    #funcao pra o butao entrar
    butaoEntrar.pack()

    labelSemCad = Label(janela, text="Não tem cadastro?", foreground="white", bg="#03467B", font="Helvetica 9 bold")
    labelSemCad.pack()

    butaoCadastrar = Button(janela,font="Helvetica 9 bold", bg='white', text="Cadastrar-se",command=cadastro)
    #funcao pra o butao cadastrar
    butaoCadastrar.pack()

    janela.geometry('300x300+500+100')

    janela.mainloop()
def auxiliar(user,senha,janela):
    if (login(user, senha) == True and user != ""):

        Frames.dashBoard(janela)
    else:
        print("aaa")
def cadastro():
    print("ENTORU")
    janela = Tk() 
    janela.iconbitmap('imagesico (2).ico')
    janela.title("Lider Prev - v3.7")
    janela['bg'] = '#03467B'
    janela.resizable(0, 0)
    janela.geometry('300x300+500+100')

    labelNomeCompleto = Label(janela, text="Nome Completo:",foreground="white", bg="#03467B", font="Helvetica 9 bold")
    labelNomeCompleto.pack()
    caixaNomeCompleto = Entry(janela, bg='white', fg='black', font="Helvetica 9 bold",)
    caixaNomeCompleto.pack()
    # nome = str(input("{:s}".format("Nome Completo: ",end="")))
    labelUser = Label(janela, text="Usuario:",foreground="white", bg="#03467B", font="Helvetica 9 bold")
    labelUser.pack()
    caixaUser = Entry(janela, bg='white', fg='black', font="Helvetica 9 bold",)
    caixaUser.pack()
    # usuario = str(input("{:s}".format("USUÁRIO: ",end="")))
    labelSenha = Label(janela, text="Senha:",foreground="white", bg="#03467B", font="Helvetica 9 bold")
    labelSenha.pack()
    caixaSenha = Entry(janela, bg='white', fg='black', font="Helvetica 9 bold",show = '*')
    caixaSenha.pack()
    # senha = getpass.getpass("SENHA: ")

    nomeCompleto = caixaNomeCompleto.get()
    user = caixaUser.get()
    senha = caixaSenha.get()

    butaoCadastrar = Button(janela,text="Cadastrar",font="Helvetica 9 bold", bg='white', command=lambda:insertUsuarios(caixaUser.get(),caixaSenha.get(),caixaNomeCompleto.get()))
    butaoCadastrar.pack()
    #butaoCadastrar["command"] = inserir(nomeCompleto,cpf,user,senha)
    janela.mainloop()