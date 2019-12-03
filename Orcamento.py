import tkinter as tk
from tkinter import*
from tkinter import ttk

import Frames
import banco


class Orcamento:

    marcas = ["Fiat", "Honda", "Volkswagen", "Chevrolet", "Toyota"]
    modelos = []
    anos = []

    lista_orcament = {"user" : 0, "preco" : 0, "marca" : 0, "modelo" : 0, "ano" : 0, "mensalidade" : 0, "acionamento" : 0}


    marca = 0
    modelo = 0
    ano = 0
    comboMarcas = 0
    comboModelo = 0
    comboAno = 0
    entrada = 0
    acionamento = 0
    mensalidade = 0
    janela2 = 0
    valor = 0
    def __init__(self):
        self.set_labels()


    def atualiza_Modelo(self, marca):
        if marca == "Honda":
            self.modelos = ["Civic", "CRV", "HRV", "Fit", "City"]
        elif marca == "Fiat":
            self.modelos = ["Uno", "Palio", "Mobi", "Doblo", "Siena", "Strada"]
        elif marca == "Volkswagen":
            self.modelos = ["Gol", "Up", "Voyage", "Fox", "Golf", "Saveiro"]
        elif marca == "Chevrolet":
            self.modelos = ["Celta", "Classic", "Corsa", "Onix", "Cruze"]
        elif marca == "Toyota":
            self.modelos = ["Corola", "Etios", "Hilux", "SW4"]
        self.comboModelo['values'] = self.modelos
        self.comboModelo.current(0)
        self.atualiza_Ano()

    def atualiza_Ano(self):

        #Depois fazer validacao
        ano = self.comboAno.get()

        for i in range(2005, 2021):
            self.anos.append(str(i))
        self.comboAno['values'] = self.anos
        self.comboAno.current(0)

    def main(self):

        self.lista_orcament["marca"] = self.comboMarcas.get()
        self.lista_orcament["modelo"] = self.comboModelo.get()
        self.lista_orcament["ano"] = self.comboAno.get()


        if self.lista_orcament["modelo"] == "" or self.lista_orcament["marca"] == "" or self.lista_orcament["ano"] == "" or self.entrada.get == "":
            print("preencha tudo")
            janela = Tk()
            janela['bg'] = '#03467B'
            janela.geometry('290x100+550+150')
            janela.title("Lider Prev - v3.7")
            janela.resizable(0, 0)
            janela.iconbitmap('imagesico (2).ico')
            labelMarca = tk.Label(janela, text="Error: Você deve preencher tudo!", font="Helvetica 12 bold", foreground="white",bg="#03467B")
            labelMarca.place(x=16,y=30)
            bt = Button(janela,text = "OK",font="Helvetica 12 bold", foreground="black",bg="white",command = janela.destroy)
            bt.place(x=125,y=60)
        else:
            try:
                self.lista_orcament["preco"] = float(self.entrada.get())
                print(self.lista_orcament["preco"])
                self.calcular(self.lista_orcament["preco"], self.lista_orcament["marca"], self.lista_orcament["modelo"], self.lista_orcament["ano"])
            except:
                print("Digite um numero animal")
                janela = Tk()
                janela['bg'] = '#03467B'
                janela.geometry('290x100+550+150')
                janela.title("Lider Prev - v3.7")
                janela.iconbitmap('imagesico (2).ico')
                labelMarca = tk.Label(janela, text="Error: Você deve preencher tudo!", font="Helvetica 12 bold",
                                      foreground="white", bg="#03467B")
                labelMarca.place(x=16, y=30)
                bt = Button(janela, text="OK", font="Helvetica 12 bold", foreground="black", bg="white",
                            command=janela.destroy)
                bt.place(x=125, y=60)

    def calcular(self, valor, marca, modelo, ano):

        self.janela2.destroy()

        self.janela2 = tk.Tk()

        janela = self.janela2


        janela['bg'] = '#03467B'
        janela.geometry('270x230+500+100')
        janela.title("Lider Prev - v3.7")
        janela.resizable(0, 0)
        janela.iconbitmap('imagesico (2).ico')

        self.lista_orcament["acionamento"] = round(valor * 0.04,2)
        self.lista_orcament["mensalidade"] = round(valor * 0.003,2)
        if  self.lista_orcament["acionamento"] < 1000 :
            self.lista_orcament["acionamento"]= 1000
            if  self.lista_orcament["mensalidade"] < 150:
                self.lista_orcament["mensalidade"] = 150

        container = Frame(janela)
        container.pack()
        container2 = Frame(janela)
        container2.pack()
        container3 = Frame(janela)
        container3.pack()
        container4 = Frame(janela)
        container4.pack()
        container5 = Frame(janela)
        container5.pack()
        container6 = Frame(jenela)
        container6.pack()

        labelMarca = tk.Label(container, text="Marca:  ", font="Helvetica 12 bold", foreground="white", bg="#03467B")
        labelMarca2 = tk.Label(container, text=marca, font="Helvetica 12 bold", foreground="white", bg="#03467B")

        labelModelo = tk.Label(container2, text="Modelo:  ", font="Helvetica 12 bold", foreground="white", bg="#03467B")
        labelModelo2 = tk.Label(container2, text=modelo, font="Helvetica 12 bold", foreground="white", bg="#03467B")

        labelAno = tk.Label(container3, text="Ano:  ", font="Helvetica 12 bold", foreground="white", bg="#03467B")
        labelAno2 = tk.Label(container3, text=ano, font="Helvetica 12 bold", foreground="white", bg="#03467B")

        labelvalor = tk.Label(container6, text="Valor:  ", font="Helvetica 12 bold", foreground="white", bg="#03467B")
        labelvalor2 = tk.Label(container6, text=valor, font="Helvetica 12 bold", foreground="white", bg="#03467B")

        # melhorar  calculo da taxa de acionamentoa.ge
        labelTaxaacionamento = tk.Label(container4, text="Taxa de acionamento:  R$", font="Helvetica 12 bold",
                                        foreground="white", bg="#03467B")
        labelTaxamensalidade = tk.Label(container4, text= self.lista_orcament["acionamento"], font="Helvetica 12 bold", foreground="white",
                                         bg="#03467B")

        # melhorar calculo da mensalidade
        labelMensalidade = tk.Label(container5, text="Mensalidade:  R$", font="Helvetica 12 bold", foreground="white",
                                    bg="#03467B")
        labelMensalidade2 = tk.Label(container5, text= self.lista_orcament["mensalidade"], font="Helvetica 12 bold", foreground="white", bg="#03467B")

        labelTop = tk.Label(janela, text="Adicionais\n\n", font="Helvetica 12 bold", foreground="white", bg="#03467B")

        labelvalor.pack(side=LEFT)
        labelvalor2.pack(side=RIGHT)
        labelMarca.pack(side=LEFT)
        labelMarca2.pack(side=RIGHT)
        labelModelo.pack(side=LEFT)
        labelModelo2.pack(side=RIGHT)
        labelAno.pack(side=LEFT)
        labelAno2.pack(side=RIGHT)
        labelTaxaacionamento.pack(side=LEFT)
        labelTaxamensalidade.pack(side=RIGHT)
        labelMensalidade.pack(side=LEFT)
        labelMensalidade2.pack(side=RIGHT)

        btvoltar = Button(janela, width=8, text="Refazer", font="Helvetica 9 bold", bg='white', command=self.voltar)
        btvoltar.place(x=90, y=199)
        btvoltar1 = Button(janela, width=8, text="Salvar", font="Helvetica 9 bold", bg='white', command=self.salvar)
        btvoltar1.place(x=190, y=199)

    def callback(self, eventObject):

        self.atualiza_Modelo(eventObject.widget.get())

    def set_labels(self):

        self.janela2 = tk.Tk()
        janela = self.janela2
        janela.resizable(0, 0)
        janela.geometry('450x275+500+100')
        janela['bg'] = '#03467B'
        janela.title("Lider Prev - v3.7")

        photo = PhotoImage(file="images (2).png")
        photo = photo.subsample(2, 2)

        label = Label(janela, image=photo, bg='#03467B')
        label.configure()
        label.place(x=230, y=40)

        self.comboMarcas = ttk.Combobox(janela, values=self.marcas, font="Helvetica 9",state = "readonly")
        self.comboModelo = ttk.Combobox(janela, values=self.modelos, font="Helvetica 9",state = "readonly")
        self.comboAno = ttk.Combobox(janela, values=self.anos, font="Helvetica 9",state = "readonly")
        self.entrada = Entry(janela, bg='white', fg='black', font="Helvetica 9 bold", width='20', textvariable="Preço")

        self.comboMarcas.place(x=20, y=40)
        self.comboMarcas.current(0)
        self.comboMarcas.bind("<<ComboboxSelected>>", self.callback)



        self.comboModelo.place(x=20, y=100)


        self.comboAno.place(x=20, y=160)


        self.entrada.place(x=20, y=220)
        janela.iconbitmap('imagesico (3).ico')
        labelTop = tk.Label(janela, text="Escolha seu modelo:", font="Helvetica 12 bold", foreground="white",
                            bg="#03467B")
        labelTop.place(x=17, y=79)
        labelTop = tk.Label(janela, text="Escolha o ano do modelo:", font="Helvetica 12 bold", foreground="white",
                            bg="#03467B")
        labelTop.place(x=17, y=139)
        labelTop = tk.Label(janela, text="Digite o valor:", font="Helvetica 12 bold ", foreground="white", bg="#03467B")
        labelTop.place(x=17, y=195)
        labelTop = tk.Label(janela, text="Escolha sua marca:", font="Helvetica 12 bold", foreground="white",
                            bg="#03467B")
        labelTop.place(x=17, y=15)

        bt3 = Button(janela, width=5, text="OK", font="Helvetica 10 bold", bg='white', command=self.main)
        bt3.place(x=397, y=243)
        btvoltar = Button(janela, width=5, text="Voltar", font="Helvetica 10 bold", bg='white', command=lambda: Frames.orcamentos(janela))
        btvoltar.place(x=332, y=243)
        #print(dict(self.comboMarcas))



        janela.mainloop()

    def voltar (self):
        self.janela2.destroy()

        self.set_labels()

    def salvar(self):

        banco.insertOrcamento(self.lista_orcament)

        self.janela2.destroy()

        self.set_labels(janela)

