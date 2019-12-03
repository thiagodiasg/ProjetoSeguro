from tkinter import *
import tkinter.filedialog

root = Tk()
menubar = Menu(root)
root.config(menu=menubar)
root.title('Tk Menu')
root.geometry('400x400')

filemenu = Menu(menubar)
filemenu2 = Menu(menubar)
filemenu3 = Menu(menubar)

menubar.add_cascade(label='Orçamento', menu=filemenu2)
menubar.add_cascade(label='Develops', menu=filemenu)
menubar.add_cascade(label='Ajuda', menu=filemenu3)

def Open(): tkFileDialog.askopenfilename()
def Save(): tkFileDialog.asksaveasfilename()
def Quit(): root.destroy()

def novoOrcamento():

    master = Tk()
    master.geometry("400x400+0+0")

    var = StringVar(master)
    var.set("MARCAS:")  # initial value

    option = OptionMenu(master, var, "FIAT", "HYUNDAY", "VW", "JEEP")
    option.pack()

    #
    # test stuff

    def ok():
        var2 = StringVar(master)
        var2.set("MODELOS:")  # initial value

        option = OptionMenu(master, var2, "FIAT", "HYUNDAY", "VW", "JEEP")
        print(type(option))


    button = Button(master, text="OK", command=ok)
    button.pack()

    mainloop()

def ColorRed(): Text(background='red').pack()
def ColorBlack(): Text(background='black').pack()
def AlterarOrcamento(): Text(background='black').pack()
def Help():
    text = Text(root)
    text.pack();
    text.insert('insert', 'Ao clicar no botão da\n'
                          'respectiva cor, o fundo da tela\n'
                          'aparecerá na cor escolhida.')

filemenu.add_command(label='Abrir...', command=Open)
filemenu.add_command(label='Salvar como...', command=Save)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=Quit)
filemenu2.add_command(label='Novo', command=novoOrcamento)
filemenu2.add_command(label='Consultar', command=ColorRed)
filemenu2.add_command(label='Apagar', command=ColorBlack)
filemenu2.add_command(label='Alterar',command=AlterarOrcamento)
filemenu3.add_command(label='Ajuda', command=Help)
root.mainloop()
