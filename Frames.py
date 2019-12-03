from tkinter import*

from Orcamento import *
from login import *


def fim(janela):
    janela.destroy()

def orcamentos(janela):
    print("dashboard")

    janela.destroy()
    janela = Tk()
    janela['bg'] = '#03467B'
    janela.title("Lider Prev - v3.7")
    janela.resizable(0, 0)
    janela.iconbitmap('imagesico (2).ico')
    lb1 = Label(janela, width = 35 , text =  "*Você pode criar um Orçamento novo ou \n consultar Orçamentos Anteriores", font="Helvetica 9 bold", foreground = "#00A654", bg = "#03467B")
    bt1 = Button(janela, width=20, text="Novo Orçamento", font="Helvetica 9 bold", bg='white', command=lambda: novoOrcamento(janela))
    bt2 = Button(janela, width=20, text="Orçamentos", font="Helvetica 9 bold", bg='white', command=lambda: updateOrcamento(janela))
    bt3 = Button(janela, width=20, text="Voltar", font="Helvetica 9 bold", bg='white',command=lambda: dashBoard(janela))
    bt1.place(x=75, y=50)
    bt2.place(x=75, y=90)
    bt3.place(x=75, y=130)
    lb1.place(x = 25, y = 250 )
    janela.geometry('300x300+500+100')
    janela.mainloop()
'''def consulta(janela):
    print("usuarios")

    janela.destroy()
    janela = Tk()
    janela.title("Lider Prev - v3.7")
    janela.iconbitmap('imagesico (2).ico')
    janela['bg'] = '#03467B'
    janela.resizable(0, 0)
    lb1 = Label(janela, width=40, text="*Buscar editar ou deletar\n  um Orçamento feito", foreground="#00A654", bg="#03467B",font="Helvetica 9 bold")
    bt1 = Button(janela, width=20, text="Buscar", font="Helvetica 9 bold", bg='white',command=lambda: updateUsuario(janela))
    bt2 = Button(janela, width=20, text="Editar", font="Helvetica 9 bold", bg='white', command=lambda: deleteOrcamento(janela))
    bt3 = Button(janela, width=20, text="Deletar", font="Helvetica 9 bold", bg='white', command=lambda: dashBoard(janela))
    bt4 = Button(janela, width=20, text="Voltar", font="Helvetica 9 bold", bg='white', command=lambda: orcamentos(janela))
    bt1.place(x=75, y=50)
    bt2.place(x=75, y=90)
    bt3.place(x=75, y=130)
    bt4.place(x=75,y = 170)
    lb1.place(x=5, y=250)
    janela.geometry('300x300+500+100')'''
def usuarios(janela):
    print("usuarios")

    janela.destroy()
    janela = Tk()
    janela['bg'] = '#03467B'
    janela.title("Lider Prev - v3.7")
    janela.resizable(0, 0)
    janela.geometry('300x300+500+100')
    janela.iconbitmap('imagesico (2).ico')
    lb1 = Label(janela, width=30, text="*Você pode editar sua senha de Usuario\n ou deletar um usuário", foreground="#00A654", bg="#03467B",font="Helvetica 9 bold")
    bt1 = Button(janela, width=20, text="Editar senha usuário", font="Helvetica 9 bold", bg='white', command=lambda: alterarSenha(janela))
    bt2 = Button(janela, width=20, text="Deletar usuário", font="Helvetica 9 bold", bg='white', command=lambda: deleteUsuario(janela))
    bt3 = Button(janela, width=20, text="Voltar", font="Helvetica 9 bold", bg='white', command = lambda: dashBoard(janela))
    bt1.place(x=75, y=50)
    bt2.place(x=75, y=90)
    bt3.place(x=75, y=130)
    lb1.place(x=45, y=250)



def dashBoard(janela):
    print("novoOrçameto")

    janela.destroy()
    janela = Tk()
    janela.iconbitmap('imagesico (2).ico')
    janela.title("Lider Prev - v3.7")
    janela.geometry('300x300+500+100')
    janela.resizable(0, 0)
    janela['bg'] = '#03467B'
    lb1 = Label(janela, width=30, text="*Você pode gerenciar Orçamentos ou\n editar sua senha de Usuario", foreground = "#00A654", bg = "#03467B",font="Helvetica 9 bold")
    bt1 = Button(janela, width=20, text="Orçamentos", font="Helvetica 9 bold", bg='white', command= lambda: orcamentos(janela))
    bt2 = Button(janela, width=20, text= "Usuarios", font="Helvetica 9 bold", bg='white', command= lambda: usuarios(janela))
    bt3 = Button(janela, width=20, text="Sair", font="Helvetica 9 bold", bg='white', command=lambda: fim(janela))
    bt1.place(x=75, y=50)
    bt2.place(x=75, y=90)
    bt3.place(x=75, y=130)
    lb1.place(x=45, y=250)




def novoOrcamento(janela):
    janela.destroy()
    orc = Orcamento()

def alterarSenha(janela):
    print("updateUsuario")
    print("deleteUsuario")
    janela.destroy()
    janela = Tk()
    janela.iconbitmap('imagesico (2).ico')
    janela.title("Lider Prev - v3.7")
    janela.resizable(0, 0)
    janela['bg'] = '#03467B'
    janela.geometry('300x300+500+100')
    lb1 = Label(janela, width=40, text="Digite a senha antiga:", foreground="white", bg="#03467B", font="Helvetica 9 bold")
    lb2 = Label(janela, width=40, text="Digite a nova senha:", foreground="white", bg="#03467B",font="Helvetica 9 bold")
    bt1 = Button(janela, width=8, text="Alterar", font="Helvetica 9 bold", bg='white', command=lambda: readOrcamento)
    bt2 = Button(janela, width=8, text="Voltar", font="Helvetica 9 bold", bg='white', command=lambda: orcamentos(janela))
    senhaAntiga = Entry(janela, bg='white', fg='black', font="Helvetica 13 bold", width='15', textvariable="id",show='*')
    senhaNova = Entry(janela, bg='white', fg='black', font="Helvetica 13 bold", width='15', textvariable="novoid",show='*')
    bt2.place(x=8, y=270)
    bt1.place(x=230, y=270)
    lb1.place(x=8, y=40)
    lb2.place(x=5, y=100)
    senhaAntiga.place(x=78, y=60)
    senhaNova.place(x=78, y=120)

def condicaoSenha(janela):
    janela = Tk()
    janela.iconbitmap('imagesico (2).ico')
    janela.title("Lider Prev - v3.7")
    janela.geometry('300x300+500+100')
    janela.resizable(0, 0)
    janela['bg'] = '#03467B'
    #if senha != senhaAntiga.get:

def updateOrcamento(janela):
    print("deleteUsuario")
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
    lb1 = Label(janela, width=40, text="Digite o ID do orçamento:", foreground="white", bg="#03467B", font="Helvetica 9 bold")
    bt1 = Button(janela, width=8, text="Buscar", font="Helvetica 9 bold", bg='white',command=lambda: readOrcamento)
    bt2 = Button(janela, width=8, text="Voltar", font="Helvetica 9 bold", bg='white',command=lambda: orcamentos(janela))
    bt3 = Button(janela, width=8, text="Deletar", font="Helvetica 9 bold", bg='white',command=lambda: deleteOrcamento())
    entrada = Entry(janela, bg='white', fg='black', font="Helvetica 9 bold", width='20', textvariable="id")
    bt2.place(x=8, y=270)
    bt3.place(x=160, y=270)
    bt1.place(x=230, y=270)
    lb1.place(x=8, y=40)
    entrada.place(x=78,y=80)
    janela.geometry('300x300+500+100')


'''def reset_janela (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    widget_list = _list
    for item in widget_list:
        item.pack_forget()'''




