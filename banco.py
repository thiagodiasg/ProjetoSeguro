import sqlite3

def createTables():
    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()
    try:
        cursor.execute("""
                CREATE TABLE usuarios(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    user TEXT NOT NULL,
                    senha varchar(12),
                    nomeCompleto varchar(50)
            );
            """)

        cursor.execute("""
                    CREATE TABLE orcamento(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        user TEXT NOT NULL,
                        preco FLOAT,
                        marca TEXT NOT NULL,
                        modelo TEXT NOT NULL,
                        ano VARCHAR(4),
                        mensalidade FLOAT, 
                        acionamento FLOAT
                    );
                """)
        print("Tabela criada")
    except:
        print("Não conseguiu criar as tabelas!! ")

def insertUsuarios(user,senha,nomeCompleto):

    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()


    cursor.execute("""
        INSERT INTO usuarios (user, senha, nomeCompleto)
            VALUES (?,?,?)
            """, (user, senha, nomeCompleto))

    conexao.commit()
    conexao.close()

def readUsuarios():

    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()

    listaUsuarios = []

    cursor.execute("""SELECT * FROM usuarios""")
    for i in cursor.fetchall():
        listaUsuarios.append(i[1])

    return listaUsuarios

#Update pra alterar senha
def updateUsuarios(novaSenha,usuario):

    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()


    cursor.execute("""
    UPDATE usuarios
    SET senha = ?
    WHERE  user = ?
    """, (novaSenha, usuario))

    conexao.commit()
    conexao.close()

def deleteUsuarios(usuarioDeletado):

    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM usuarios
    WHERE user = ?
    """, (usuarioDeletado,))

    conexao.commit()
    conexao.close()

def insertOrcamento():
    #

    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO orcamento (user, preco, marca, modelo, ano, mensalidade, acionamento)
        VALUES (?,?,?,?,?,?,?)
        """, (dicio["user"], dicio["preco"], dicio["marca"], dicio["modelo"], dicio["ano"], dicio["mensalidade"], dicio["acionamento"]))

    conexao.commit()
    conexao.close()
def readOrcamento():

    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()

    cursor.execute("""SELECT * FROM orcamento""")
    for i in cursor.fetchall():
        print(i)
def deleteOrcamento(orcamentoDeletado):

    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM orcamento
    WHERE user = ?
    """, (orcamentoDeletado,))

    conexao.commit()
    conexao.close()

def login(usuario,senha):
    verificaSenha = 000
    verificaUser = 'Nulo'

    conexao = sqlite3.connect('liderPrev.db')
    cursor = conexao.cursor()

    cursor.execute("""
SELECT senha FROM usuarios
WHERE user = ?
""", (usuario,))

    x = cursor.fetchall()
    if len(x) > 0:
        verificaSenha = x[0][0]

    cursor.execute("""
  SELECT user FROM usuarios
  WHERE user = ?
  """, (usuario,))

    x = cursor.fetchall()
    if len(x) > 0:
        verificaUser = x[0][0]

    if senha == verificaSenha and verificaUser == usuario:
        return True
    else:
        return False
