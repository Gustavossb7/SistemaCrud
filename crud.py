import mysql.connector
from tkinter import *
from tkinter.font import Font

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sorvetes',
    database='bdyoutube',
)

cursor = conexao.cursor()

janela = Tk()

#CRUD
def create():
    #CREATE
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sorvetes',
        database='bdyoutube',
    )


    cursor = conexao.cursor()
    nome = entrada.get()
    valor = entrada2.get()
    print(nome)
    print(valor)
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome}", {valor})'
    cursor.execute(comando)
    conexao.commit() #Edita o banco de dados

#READ
def read():

    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sorvetes',
        database='bdyoutube',
    )

    cursor = conexao.cursor()
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall() #Lê o banco de dados
    print(resultado)

    texto_update["text"] = resultado

#UPDATE
def update():

    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sorvetes',
        database='bdyoutube',
    )

    cursor = conexao.cursor()

    nome = entrada3.get()
    valor = entrada4.get()
    print(f"O valor de {nome} foi alterado para {valor}")
    comando = f'UPDATE vendas SET valor = "{valor}" WHERE nome_produto = "{nome}"'
    cursor.execute(comando)
    conexao.commit() #Edita o banco de dados

#DELETE
def delete():

    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sorvetes',
        database='bdyoutube',
    )

    cursor = conexao.cursor()

    nome = entrada5.get()
    print(nome)
    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome}"'
    cursor.execute(comando)
    conexao.commit() #Edita o banco de dados


janela.title('Nome do CRUD')

my_font = Font(family="Times New Roman", size=24)
my_font2 = Font(family="Times New Roman", size=18)
my_font3 = Font(family="Times New Roman", size=12)


texto_orientacao5 = Label(janela, text="Cadastro de produtos", font=my_font)
texto_orientacao5.grid(column=1, row=0, padx=30, pady=30)


texto_orientacao = Label(janela, text="Create", font=my_font2)
texto_orientacao.grid(column=0, row=1, padx=10, pady=10)

botao = Button(janela, text='            ', command=create)
botao.grid(column=0, row=2, padx=10, pady=10)

entrada = Entry(janela, width=10)
entrada.grid(row=2, column=1, padx=10, pady=10)

texto_orientacao5 = Label(janela, text="Nome do produto", font=my_font3)
texto_orientacao5.grid(column=1, row=1, padx=10, pady=10)

entrada2 = Entry(janela, width=10)
entrada2.grid(row=2, column=2, padx=10, pady=10)

texto_orientacao6 = Label(janela, text="Valor", font=my_font3)
texto_orientacao6.grid(column=2, row=1, padx=10, pady=10)






texto_orientacao2 = Label(janela, text="Update", font=my_font2)
texto_orientacao2.grid(column=0, row=3, padx=10, pady=10)

botao2 = Button(janela, text='            ', command=update)
botao2.grid(column=0, row=4, padx=10, pady=10)

entrada3 = Entry(janela, width=10)
entrada3.grid(row=4, column=1, padx=10, pady=10)

entrada4 = Entry(janela, width=10)
entrada4.grid(row=4, column=2, padx=10, pady=10)





texto_orientacao3 = Label(janela, text="Delete", font=my_font2)
texto_orientacao3.grid(column=0, row=5, padx=10, pady=10)

botao3 = Button(janela, text='            ', command=delete)
botao3.grid(column=0, row=6, padx=10, pady=10)

entrada5 = Entry(janela, width=10)
entrada5.grid(row=6, column=1, padx=10, pady=10)






texto_orientacao4 = Label(janela, text="Read", font=my_font2)
texto_orientacao4.grid(column=0, row=7, padx=10, pady=10)

botao4 = Button(janela, text='            ', command=read)
botao4.grid(column=0, row=8, padx=10, pady=10)



texto_update = Label(janela, text="")
texto_update.grid(column=1, row=9, padx=10, pady=10)



cursor.close()
conexao.close()



janela.mainloop()