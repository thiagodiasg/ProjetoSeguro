from tkinter import *
import os


# Define a função de cadastro
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.resizable(0, 0)
    register_screen.title("Cadastrar Novo Cliente")
    register_screen.geometry("900x600+120+130")
    register_screen.configure(bg='gray17')

    global name
    global idade
    global email
    global cpf
    global rg
    global sexo
    global data_cadastro
    global code_client
    global vencimento
    global vencimento_entry
    global name_entry
    global idade_entry
    global email_entry
    global sexo_entry
    global data_cadastro_entry
    global cpf_entry
    global code_client_entry
    global rg_entry

    name = StringVar()
    idade = StringVar()
    email = StringVar()
    sexo = StringVar()
    data_cadastro = StringVar()
    code_client = StringVar()
    cpf = StringVar()
    rg = StringVar()
    vencimento = StringVar()

    Label(register_screen, text="Cadastre os dados abaixo", bg="gray17", fg='white', width="300", height="1",
          font=("Calibri", 13)).pack()

    name_lable = Label(register_screen, text="Nome:", bg="gray17", fg='white')
    name_lable.place(x=5, y=50)

    name_entry = Entry(register_screen, bg='gray30', fg='white', width='40', textvariable=name)
    name_entry.place(x=50, y=50)

    idade_label = Label(register_screen, text='Idade:', bg="gray17", fg='white')
    idade_label.place(x=320, y=50)

    idade_entry = Entry(register_screen, bg='gray30', fg='white', width='5', textvariable=idade)
    idade_entry.place(x=390, y=50)

    email_label = Label(register_screen, text="Email:", bg="gray17", fg='white')
    email_label.place(x=5, y=100)

    email_entry = Entry(register_screen, width='40', bg='gray30', fg='white', textvariable=email)
    email_entry.place(x=50, y=100)

    sexo_label = Label(register_screen, text='Sexo(M/F):', bg='gray17', fg='white')
    sexo_label.place(x=320, y=100)

    sexo_entry = Entry(register_screen, width='5', bg='gray30', fg='white', textvariable=sexo)
    sexo_entry.place(x=390, y=100)

    data_cadastro_label = Label(register_screen, text="Data do Cadastro:", bg="gray17", fg='white')
    data_cadastro_label.place(x=460, y=50)

    data_cadastro_entry = Entry(register_screen, width='15', bg='gray30', fg='white', textvariable=data_cadastro)
    data_cadastro_entry.place(x=570, y=50)

    code_client_label = Label(register_screen, text='Código:', bg='gray17', fg='white')
    code_client_label.place(x=460, y=100)

    code_client_entry = Entry(register_screen, width='15', bg='gray30', fg='white', textvariable=code_client)
    code_client_entry.place(x=570, y=100)

    cpf_entry_label = Label(register_screen, text='CPF:', bg='gray17', fg='white')
    cpf_entry_label.place(x=5, y=150)

    cpf_entry = Entry(register_screen, width='40', bg='gray30', fg='white', textvariable=cpf)
    cpf_entry.place(x=50, y=150)

    rg_label = Label(register_screen, text='RG:', bg='gray17', fg='white')
    rg_label.place(x=320, y=150)

    rg_entry = Entry(register_screen, width='15', bg='gray30', fg='white', textvariable=rg)
    rg_entry.place(x=390, y=150)

    vencimento_label = Label(register_screen, text='Vencimento:', bg='gray17', fg='white')
    vencimento_label.place(x=690, y=50)

    vencimento_entry = Entry(register_screen, bg='gray30', fg='white', width='15', textvariable=vencimento)
    vencimento_entry.place(x=775, y=50)

    finalizar = Button(register_screen, text="Finalizar", width='20', height='1', bg="gray30", fg='white',
                       command=register_user)

    voltar = Button(register_screen, text='Cancelar', bg='gray30', fg='white', width='10', height='1',
                    command=delete_register)

    voltar.pack(side=BOTTOM)
    Label(register_screen, text='', bg='gray17', height='1').pack(side=BOTTOM)
    finalizar.pack(side=BOTTOM)


# Função de realizar o cadastro no sistema e criar o arquivo com as informações
def register_user():
    name_info = name.get()
    idade_info = idade.get()
    email_info = email.get()
    sexo_info = sexo.get()
    data_cad_info = data_cadastro.get()
    code_info = code_client.get()
    cpf_info = cpf.get()
    rg_info = rg.get()
    vencimento_info = vencimento.get()

    file = open(code_info, "w")
    file.write(code_info + "\n")
    file.write(name_info + "\n")
    file.write(idade_info + "\n")
    file.write(sexo_info + "\n")
    file.write(data_cad_info + "\n")
    file.write(email_info + '\n')
    file.write(cpf_info + '\n')
    file.write(rg_info + '\n')
    file.write(vencimento_info + '\n')

    file.close()

    name_entry.delete(0, END)
    idade_entry.delete(0, END)
    sexo_entry.delete(0, END)
    email_entry.delete(0, END)
    data_cadastro_entry.delete(0, END)
    cpf_entry.delete(0, END)
    rg_entry.delete(0, END)
    vencimento_entry.delete(0, END)

    # list_of_files = os.listdir()

    success_register()


# Função de editar o cadastro/arquivo de informações
def edit_register_user():
    name_info = name.get()
    idade_info = idade.get()
    email_info = email.get()
    sexo_info = sexo.get()
    data_cad_info = data_cadastro.get()
    code_info = code_client.get()
    cpf_info = cpf.get()
    rg_info = rg.get()
    vencimento_info = vencimento.get()

    file = open(code_info, "w")
    file.write(code_info + "\n")
    file.write(name_info + "\n")
    file.write(idade_info + "\n")
    file.write(sexo_info + "\n")
    file.write(data_cad_info + "\n")
    file.write(email_info + '\n')
    file.write(cpf_info + '\n')
    file.write(rg_info + '\n')
    file.write(vencimento_info + '\n')

    file.close()

    name_entry.delete(0, END)
    idade_entry.delete(0, END)
    sexo_entry.delete(0, END)
    email_entry.delete(0, END)
    data_cadastro_entry.delete(0, END)
    cpf_entry.delete(0, END)
    rg_entry.delete(0, END)
    vencimento_entry.delete(0, END)
    code_client_entry.delete(0, END)

    success_edit_register()


# Popup que informa o sucesso ao realizar o cadastro
def success_register():
    global you_are_register_now
    you_are_register_now = Toplevel(register_screen)
    you_are_register_now.resizable(0, 0)
    you_are_register_now.title('Nice!!')
    you_are_register_now.geometry("250x110+460+400")
    you_are_register_now.configure(bg='gray17')

    Label(you_are_register_now, text="Cadastro realizado com sucesso.", bg='gray17', fg='white', height='3').pack()
    Label(you_are_register_now, text='', bg='gray17')

    Button(you_are_register_now, text="OK", bg='gray30', fg='white', command=delete_register).pack()


# Popup que informa o sucesso ao editar o cadastro
def success_edit_register():
    global you_are_edited_now
    you_are_edited_now = Toplevel(edit_register_screen)
    you_are_edited_now.resizable(0, 0)
    you_are_edited_now.title('Nice!!')
    you_are_edited_now.geometry("250x110+460+400")
    you_are_edited_now.configure(bg='gray17')

    Label(you_are_edited_now, text="Cadastro editado com sucesso.", bg='gray17', fg='white', height='3').pack()
    Label(you_are_edited_now, text='', bg='gray17')

    Button(you_are_edited_now, text="OK", bg='gray30', fg='white', command=delete_edit_register).pack()


'''
def due_date():
    code_entry5 = client_verify.get()

    due_date_file = os.listdir()
    file3 = open(code_entry5, "r")
    #Lê o arquivo e divide as linhas em lista
    verify3 = file3.read().splitlines()
    verify3[8].split('/')
'''


# Função de verificaçõa: Verifica se o codigo que foi digitado em
# start_access() está cadastrado no sistema
def login_verify():
    global list_of_files
    global code_entry1

    code_entry1 = client_verify.get()

    list_of_files = os.listdir()

    # Realiza da verificação do código
    if code_entry1 in list_of_files:
        show_info_access()
        access_allowed()
    else:
        access_denied()


# Informa acesso negado, caso o codigo não esteja cadastrado no sistema
def access_denied():
    code_entry.delete(0, END)

    def countdown(time):
        if time == -1:
            popup.destroy()
        else:
            popup.after(500, countdown, time - 1)

    popup = Toplevel(access_permission)
    popup.geometry('300x200+950+300')
    popup.configure(bg='gray17')

    Label(popup, text='', bg='gray17', height='5').pack()

    label = Label(popup, text='Acesso negado', bg='gray17', fg='red', font=('calibri', 15)).pack()
    countdown(2)

    popup.mainloop()


# Informa acesso permitido, caso o codigo esteja cadastrado no sistema
def access_allowed():
    code_entry.delete(0, END)

    def countdown(time):
        if time == -1:
            popup.destroy()
        else:
            popup.after(500, countdown, time - 1)

    popup = Toplevel(access_permission)
    popup.geometry('300x200+950+300')
    popup.configure(bg='gray17')

    Label(popup, text='', bg='gray17', height='5').pack()

    label = Label(popup, text='Acesso permitido', bg='gray17', fg='#20FD3A', font=('calibri', 15)).pack()

    countdown(2)
    popup.mainloop()


# Define a tela de "login" com o código do cliente
def start_access():
    global access_permission
    global client_verify
    global code_entry

    access_permission = Toplevel(main_screen)
    access_permission.resizable(0, 0)
    access_permission.title('Academia GG EZ')
    access_permission.configure(bg='gray17')
    access_permission.geometry('300x200+950+300')

    Label(access_permission, bg='gray17').pack()

    client_verify = StringVar()

    code_entry = Entry(access_permission, bg='gray40', fg='white', width='30', textvariable=client_verify)
    code_entry.pack()

    Label(access_permission, bg='gray17').pack()

    # Envia o codigo digitado para a função de verificação
    confirm_bt = Button(access_permission, text='Ok', width='3', height='1', bg='gray30', fg='white',
                        command=login_verify)
    confirm_bt.pack()

    Label(access_permission, bg='gray17', height='5').pack()

    fechar_bt = Button(access_permission, text='Fechar', width='5', height='1', bg='gray30', fg='white',
                       command=delete_start_access)
    fechar_bt.pack()


# Define a tela para procurar o codigo/arquivo para editar
def select_file():
    global code_select
    global select_file_screen

    code_select = StringVar()

    select_file_screen = Toplevel(main_screen)
    select_file_screen.resizable(0, 0)
    select_file_screen.title('Editar cadastro')
    select_file_screen.configure(bg='gray17')
    select_file_screen.geometry('300x200+450+300')
    Label(select_file_screen, text='Digite o número do cadastro', bg='gray17', fg='white', height='3').pack()

    select_entry = Entry(select_file_screen, bg='gray40', fg='white', textvariable=code_select)
    select_entry.pack()
    Label(select_file_screen, text='', bg='gray17').pack()
    select_bt = Button(select_file_screen, text='Ok', bg='gray30', fg='white', width='5', command=edit_register)
    select_bt.pack()


# Define a tela de editar cadastro
def edit_register():
    global edit_register_screen
    code_entry3 = code_select.get()
    list_of_files3 = os.listdir()

    # Verifica se o código digitasdo está cadastrado
    if code_entry3 in list_of_files3:

        # Abre o arquivo com o nome do código digitado
        # em modo "r"(read)
        file2 = open(code_entry3, "r")

        # Lê o arquivo e divide as linhas em lista
        verify2 = file2.read().splitlines()

        select_file_screen.destroy()

        edit_register_screen = Toplevel(main_screen)
        edit_register_screen.resizable(0, 0)

        edit_register_screen.geometry("900x600+120+130")
        edit_register_screen.title("Academia GG EZ")

        edit_register_screen.configure(bg='gray17')

        global name
        global idade
        global email
        global cpf
        global rg
        global sexo
        global data_cadastro
        global code_client
        global vencimento
        global vencimento_entry
        global name_entry
        global idade_entry
        global email_entry
        global sexo_entry
        global data_cadastro_entry
        global cpf_entry
        global code_client_entry
        global rg_entry

        name = StringVar()
        idade = StringVar()
        email = StringVar()
        sexo = StringVar()
        data_cadastro = StringVar()
        code_client = StringVar()
        cpf = StringVar()
        rg = StringVar()
        vencimento = StringVar()

        # Adiciona nas entradas os indices da lista que foi dividida acima
        # Ex.:  .insert(0, verify2[1]) / 0 = posição onde vai inserir o item / verify[1] = Adiciona
        # o indice 1 da lista verify, que neste caso é o nome.

        Label(edit_register_screen, text="Editar cadastro", bg="gray17", fg='white', width="300", height="1",
              font=("Calibri", 13)).pack()

        name_lable = Label(edit_register_screen, text="Nome:", bg="gray17", fg='white')
        name_lable.place(x=5, y=50)

        name_entry = Entry(edit_register_screen, bg='gray30', fg='white', width='40', textvariable=name)
        name_entry.place(x=50, y=50)
        name_entry.insert(0, verify2[1])

        idade_label = Label(edit_register_screen, text='Idade:', bg="gray17", fg='white')
        idade_label.place(x=320, y=50)

        idade_entry = Entry(edit_register_screen, bg='gray30', fg='white', width='5', textvariable=idade)
        idade_entry.place(x=390, y=50)
        idade_entry.insert(0, verify2[2])

        email_label = Label(edit_register_screen, text="Email:", bg="gray17", fg='white')
        email_label.place(x=5, y=100)

        email_entry = Entry(edit_register_screen, width='40', bg='gray30', fg='white', textvariable=email)
        email_entry.place(x=50, y=100)
        email_entry.insert(0, verify2[5])

        sexo_label = Label(edit_register_screen, text='Sexo(M/F):', bg='gray17', fg='white')
        sexo_label.place(x=320, y=100)

        sexo_entry = Entry(edit_register_screen, width='5', bg='gray30', fg='white', textvariable=sexo)
        sexo_entry.place(x=390, y=100)
        sexo_entry.insert(0, verify2[3])

        data_cadastro_label = Label(edit_register_screen, text="Data do Cadastro:", bg="gray17", fg='white')
        data_cadastro_label.place(x=460, y=50)

        data_cadastro_entry = Entry(edit_register_screen, width='15', bg='gray30', fg='white',
                                    textvariable=data_cadastro)
        data_cadastro_entry.place(x=570, y=50)
        data_cadastro_entry.insert(0, verify2[4])

        code_client_label = Label(edit_register_screen, text='Código:', bg='gray17', fg='white')
        code_client_label.place(x=460, y=100)

        code_client_entry = Entry(edit_register_screen, width='15', bg='gray30', fg='white', textvariable=code_client)
        code_client_entry.place(x=570, y=100)
        code_client_entry.insert(0, code_entry3)

        cpf_entry_label = Label(edit_register_screen, text='CPF:', bg='gray17', fg='white')
        cpf_entry_label.place(x=5, y=150)

        cpf_entry = Entry(edit_register_screen, width='40', bg='gray30', fg='white', textvariable=cpf)
        cpf_entry.place(x=50, y=150)
        cpf_entry.insert(0, verify2[6])

        rg_label = Label(edit_register_screen, text='RG:', bg='gray17', fg='white')
        rg_label.place(x=320, y=150)

        rg_entry = Entry(edit_register_screen, width='15', bg='gray30', fg='white', textvariable=rg)
        rg_entry.place(x=390, y=150)
        rg_entry.insert(0, verify2[7])

        vencimento_label = Label(edit_register_screen, text='Vencimento:', bg='gray17', fg='white')
        vencimento_label.place(x=690, y=50)

        vencimento_entry = Entry(edit_register_screen, bg='gray30', fg='white', width='15', textvariable=vencimento)
        vencimento_entry.place(x=775, y=50)
        vencimento_entry.insert(0, verify2[8])

        finalizar = Button(edit_register_screen, text="Finalizar", width='20', height='1', bg="gray30", fg='white',
                           command=edit_register_user)

        voltar = Button(edit_register_screen, text='Cancelar', bg='gray30', fg='white', width='10', height='1',
                        command=delete_edit_register)

        voltar.pack(side=BOTTOM)
        Label(edit_register_screen, text='', bg='gray17', height='1').pack(side=BOTTOM)
        finalizar.pack(side=BOTTOM)

    # Informa que o código não está cadastrado
    else:
        popup2 = Toplevel(main_screen)
        popup2.geometry('300x200+450+300')
        popup2.configure(bg='gray17')

        # Popup automatico
        def countdown(time):
            if time == -1:
                popup2.destroy()
            else:
                popup2.after(500, countdown, time - 1)

        Label(popup2, text='', bg='gray17', height='5').pack()

        label = Label(popup2, text='Código não localizado', bg='gray17', fg='red', font=('calibri', 14)).pack()

        countdown(2)
        popup2.mainloop()


# informações sobre o aplicativo
def app_info():
    global app_info_screen

    app_info_screen = Toplevel(main_screen)
    app_info_screen.resizable(0, 0)
    app_info_screen.title('Informações')
    app_info_screen.geometry("900x600+120+130")
    app_info_screen.configure(bg='gray17')

    Label(app_info_screen, bg='gray17', height='7').pack()

    Label(app_info_screen,
          text='Aplicativo desenvolvido para projeto universitário.\nDesenvolvido por:\n\nThalison Vinícius\nNatália\nDandara\nMikaelle\nLudmila',
          bg='gray17', fg='white', height='20').pack()

    Button(app_info_screen, text='Voltar', bg='gray30', fg='white', command=delete_app_info).pack()


# Adiciona o nome na ListBox
def show_info_access():
    code_entry2 = client_verify.get()
    list_of_files2 = os.listdir()



    if code_entry2 in list_of_files2:
        file1 = open(code_entry2, "r")
        verify = file1.read().splitlines()

        add_nome = verify[1].split()

        for i in range (len(lista_nomes)):
            if verify[0] in lista_nomes[i][0]:
                del(lista_nomes[i])

                list_clients2 = Listbox(main_screen, width=30, height=28, bg='gray25', fg='#20FD3A', font=("Helvetica", 12))
                list_clients2.pack(side=LEFT, fill="y")

            elif i == len(lista_nomes):
                list_clients.insert(END, '{} - {}'.format(verify[0], add_nome[0]))
                lista_nomes.insert((verify[0], add_nome[0]))

        for x in range(len(lista_nomes)):
            list_clients2.insert(END, '{} - {}'.format(lista_nomes[x][0], lista_nomes[x][1]))



        list_clients = list_clients2









# Deleta popups e screens
def delete_start_access():
    access_permission.destroy()


def delete_app_info():
    app_info_screen.destroy()


def delete_register():
    register_screen.destroy()


def delete_edit_register():
    edit_register_screen.destroy()


# Define a janela inicial
class Screen:

    list_clients = 0

    def __init__(self):
        self.main_account_screen()

    def main_account_screen(self):
        global main_screen


        main_screen = Tk()
        main_screen.resizable(0, 0)

        main_screen.geometry("900x600+120+130")
        main_screen.title("Academia GG EZ")

        main_screen.configure(bg='gray17')

        info_btt = Button(main_screen, text='?', width='4', bg='gray30', fg='white', command=app_info)
        info_btt.place(x=220, y=572)

        iniciar = Button(main_screen, text='Iniciar', width='5', bg='gray30', fg='white', command=start_access)
        iniciar.place(x=852, y=572)

        cad_bt = Button(main_screen, text='Cadastrar novo cliente', bg='gray30', fg='white', command=register)
        cad_bt.place(x=632, y=572)

        self.list_clients = Listbox(main_screen, width=30, height=28, bg='gray25', fg='#20FD3A', font=("Helvetica", 12))
        self.list_clients.pack(side=LEFT, fill="y")

        Label(self.list_clients, text='LISTA DE ENTRADA:', bg='gray20', fg='white', width=30).pack()

        edit_bt = Button(main_screen, text='Editar cadastro', bg='gray30', fg='white', command=select_file)
        edit_bt.place(x=762, y=572)

        scrollbar = Scrollbar(self.list_clients, orient="vertical")
        scrollbar.config(command=self.list_clients.yview)
        scrollbar.pack(side=RIGHT, fill="y")

        self.list_clients.configure(yscrollcommand=scrollbar.set)

        self.list_clients.insert(0, '')

        main_screen.mainloop()

    def funcao1(self):
        print()

    def funcao2(self):
        print()

lista_nomes = []

tela = Screen()