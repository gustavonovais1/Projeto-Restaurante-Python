from distutils.command.build import build
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from turtle import color, pen, update
from matplotlib.pyplot import gray, grid
from numpy import append, pad
import pymysql
from tkinter import messagebox


class AdminJanela():

    def cadastrarProduto(self):
        self.cadastar = Tk()
        self.cadastar.title('Cadastro de produtos')
        self.cadastar['bg'] = '#524f4f'

        Label(self.cadastar, text='Cadastre os produtos', bg='#524f4f' , fg='white').grid(row=0, column=0,columnspan=4, padx=5, pady=5)

        Label(self.cadastar, text='Nome', bg='#524f4f' , fg='white').grid(row=1, column=0,columnspan=1, padx=5, pady=5)
        self.nome = Entry(self.cadastar)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.cadastar, text='Engredientes', bg='#524f4f' , fg='white').grid(row=2, column=0,columnspan=1, padx=5, pady=5)
        self.ingredientes = Entry(self.cadastar)
        self.ingredientes.grid(row=2, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.cadastar, text='Grupo', bg='#524f4f' , fg='white').grid(row=3, column=0,columnspan=1, padx=5, pady=5)
        self.grupo = Entry(self.cadastar)
        self.grupo.grid(row=3, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.cadastar, text='Preço', bg='#524f4f' , fg='white').grid(row=4, column=0,columnspan=1, padx=5, pady=5)
        self.preco = Entry(self.cadastar)
        self.preco.grid(row=4, column=1, columnspan=2, padx=5 ,  pady=5)

        Button(self.cadastar , text='Cadastrar', width=15, bg='gray', relief='flat', command=self.CadastrarProdutoBackAnd, highlightbackground='#524f4f').grid(row=5, column=0 , padx=5, pady=5)
        Button(self.cadastar , text='Excluir', width=15, bg='gray', relief='flat', command=self.RemoverProdutosBackAnd, highlightbackground='#524f4f').grid(row=5, column=1 , padx=5, pady=5)
        Button(self.cadastar , text='Atualizar', width=15, bg='gray', relief='flat',command=self.CadastrarProdutoBackAnd, highlightbackground='#524f4f').grid(row=6, column=0 , padx=5, pady=5)
        Button(self.cadastar , text='Limpar produtos', width=15, bg='gray', relief='flat', command=self.LimpaCadastrosBackAnd, highlightbackground='#524f4f').grid(row=6, column=1 , padx=5, pady=5)

        self.tree = ttk.Treeview(self.cadastar, selectmode='browse', column=('coluna1', 'coluna2', 'coluna3', 'coluna4'), show='headings')

        self.tree.column('coluna1', width=200, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column('coluna2', width=400, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Engredientes')

        self.tree.column('coluna3', width=200, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column('coluna4', width=60, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Preço')

        self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=3, rowspan=6)

        self.MostrarProdutosBackAnd()

        self.cadastar.mainloop()

    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)                                                                                                                                                                                                                                                   
        self.root.title('ADMIN')

        Button(self.root, text='Produtos', width=20, bg='#4682B4', command=self.CadastrarPedidos).grid(row=0, column=0, padx=10, pady=10)
        Button(self.root, text='Cadastros', width=20, bg='#B0C4DE', command=self.cadastrarProduto).grid(row=1, column=0, padx=10, pady=10)
        Button(self.root, text='Vizualizar cadastros' , width=20, bg='white',command= self.vizualizarCadastros).grid(row=6, column=0,  padx=5, pady=5, columnspan=2,)
        Button(self.root, text='Vizualizar pedidos' , width=20, bg='white', command=self.VizualizarPedidos).grid(row=7, column=0,  padx=5, pady=5, columnspan=2,)

        self.root.mainloop()

    def MostrarProdutosBackAnd(self):
        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Erro ao conectar ao banco de dados')     

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('select *from produtos')
                resultados = Cursor.fetchall()
        
        except: 
            print('Erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children()) 

        linhav = []

        for linha in resultados:
            linhav.append(linha['nome'])
            linhav.append(linha['ingredientes'])
            linhav.append(linha['grupo'])
            linhav.append(linha['preco'])
            
            self.tree.insert('', END, values=linhav, iid=linha['id'], tags='1')

            linhav.clear()

    def MostrarPedidosBackAnd(self):

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Erro ao conectar ao banco de dados')     

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('select *from pedidos')
                resultados = Cursor.fetchall()

        except: 
            print('Erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children()) 

        linhav = []

        for linha in resultados:
            linhav.append(linha['nome'])
            linhav.append(linha['grupo'])
            linhav.append(linha['ingredientes'])
            linhav.append(linha['localEntrega'])
            linhav.append(linha['observacoes'])
            
            self.tree.insert('', END, values=linhav, iid=linha['id'], tags='1')

            linhav.clear()


    def CadastrarProdutoBackAnd(self):
        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Erro ao conectar ao banco de dados')     

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('insert into produtos (nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)', (nome, ingredientes, grupo, preco))
                conexao.commit()
        
        except: 
            print('Erro ao fazer a consulta')

        self.MostrarProdutosBackAnd()

    def RemoverProdutosBackAnd(self):
        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('delete from produtos where id = {}'.format(idDeletar))
                conexao.commit()
        
        except: 
            print('Erro ao fazer a consulta')

        self.MostrarProdutosBackAnd()

    def RemoverPedidosBackAnd(self):

        idDeletar = int(self.tree.selection()[0])

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                conexao.commit()
                
        except: 
            print('Erro ao fazer a consulta')

        self.MostrarPedidosBackAnd()
        

    def LimpaCadastrosBackAnd(self):
        if messagebox.showinfo('Limpar dados, CUIDADO!', 'DESEJA EXCLUIR TODOS OS DADOS? Não será possível a restalração'):
            
            try:
                conexao = pymysql.connect(
                
                    host='localhost',
                    user='root',
                    password='',
                    db='erp',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor     
                
                )
            except:
                print('Erro ao conectar ao banco de dados')

            try:
                with conexao.cursor() as Cursor:
                    Cursor.execute('truncate table produtos;')
                    conexao.commit()
        
            except: 
                print('Erro ao fazer a consulta')

            self.MostrarProdutosBackAnd()

    def vizualizarCadastros(self):
        self.tv = Toplevel()

        self.tv.title('Vizualizar cadastros')

        self.tree = ttk.Treeview(self.tv, selectmode='browse', column=('coluna1', 'coluna2', 'coluna3', 'coluna4', 'coluna5'), show='headings')

        self.tree.column('coluna1', width=40, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='ID')

        self.tree.column('coluna2', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Usuario')

        self.tree.column('coluna3', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Senha')

        self.tree.column('coluna4', width=40, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Nivel')

        self.tree.column('coluna5', width=40, minwidth=500, stretch=NO)
        self.tree.heading('#5', text='Nivel')

        self.tree.grid(row=0, column=0, padx=10, pady=10)

        self.updateBackAnd()    

        self.vc.mainloop()  

    def updateBackAnd(self):
        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('select * from cadastros')
                resultados = Cursor.fetchall()
        
        except: 
            print('Erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhav = []

        for linha in resultados:
            linhav.append(linha['id'])
            linhav.append(linha['nome'])
            linhav.append(linha['senha'])
            linhav.append(linha['nivel'])

            self.tree.insert('', END ,values=linhav, iid=linha['id'],  tag='1')

            linhav.clear()

    def upedatepedidosBackAnd(self):

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Erro ao conectar ao banco de dados')

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('select * from pedidos')
                resultados = Cursor.fetchall()
        
        except: 
            print('Erro ao fazer a consulta')

        self.tree.delete(*self.tree.get_children())

        linhav = []

        for linha in resultados:
            linhav.append(linha['nome'])
            linhav.append(linha['grupo'])
            linhav.append(linha['ingredientes'])
            linhav.append(linha['localEntrega'])
            linhav.append(linha['observacoes'])

            self.tree.insert('', END ,values=linhav, iid=linha['id'],  tag='1')

            linhav.clear()

    def CadastrarPedidos(self):
        self.pedidos = Tk()
        self.pedidos['bg'] = '#4682B4'
        self.pedidos.title('Enserir pedidos')

        Label(self.pedidos, text='Cadastre os produtos', bg='#4682B4' , fg='white').grid(row=0, column=0,columnspan=4, padx=5, pady=5)

        Label(self.pedidos, text='Nome', bg='#4682B4' , fg='white').grid(row=1, column=0,columnspan=1, padx=5, pady=5)
        self.nome = Entry(self.pedidos)
        self.nome.grid(row=1, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.pedidos, text='Engredientes', bg='#4682B4' , fg='white').grid(row=2, column=0,columnspan=1, padx=5, pady=5)
        self.ingredientes = Entry(self.pedidos)
        self.ingredientes.grid(row=2, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.pedidos, text='Grupo', bg='#4682B4' , fg='white').grid(row=3, column=0,columnspan=1, padx=5, pady=5)
        self.grupo = Entry(self.pedidos)
        self.grupo.grid(row=3, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.pedidos, text='IocalEntrega', bg='#4682B4' , fg='white').grid(row=4, column=0,columnspan=1, padx=5, pady=5)
        self.localEntrega = Entry(self.pedidos)
        self.localEntrega.grid(row=4, column=1, columnspan=2, padx=5 ,  pady=5)

        Label(self.pedidos, text='observações', bg='#4682B4' , fg='white').grid(row=5, column=0,columnspan=1, padx=5, pady=5)
        self.observacoes = Entry(self.pedidos)
        self.observacoes.grid(row=5, column=1, columnspan=2, padx=5 ,  pady=5)

        Button(self.pedidos, text='Enviar', width=15, command=self.CadastrarPedidosBackAnd).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.pedidos.mainloop()

    def CadastrarPedidosBackAnd(self):
        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        localEntrega = self.localEntrega.get()
        observacoes = self.observacoes.get()

        try:
        
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
            
        except:
            print('Erro ao conectar ao banco de dados')     

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes) values (%s, %s, %s, %s, %s)', (nome, ingredientes, grupo, localEntrega, observacoes))
                conexao.commit()
            messagebox.showinfo('Sucesso' , 'Pedido enviado com exito!')
        except: 
            print('Erro ao fazer a consulta')

    def VizualizarPedidos(self):
        self.tv = Toplevel()
        self.tv.resizable(False, False)
        self.tv.title('Vizualizar cadastros')

        self.tree = ttk.Treeview(self.tv, selectmode='browse', column=('coluna1', 'coluna2', 'coluna3', 'coluna4'), show='headings')

        self.tree.column('coluna1', width=50, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column('coluna2', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column('coluna3', width=50, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column('coluna4', width=150, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='IocalEntrega')

        self.tree.column('coluna4', width=100, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Observações')

        self.tree.grid(row=0, column=0, padx=10, pady=10)

        

        Button(self.tv, text='Excluir pedido' , command=self.RemoverPedidosBackAnd, width=15).grid(row=1, column=0, padx=10, pady=10)

        self.upedatepedidosBackAnd()

        self.tv.mainloop()

class JanelaLogin():

    def VerificaLogin(self):
        altenticado = False
        usuarioMaster = False

        try:
            conexao = pymysql.connect(
                
                host='localhost',
                user='root',
                password='',
                db='erp',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor     
                
            )
        except:
            print('Erro ao conectar ao banco de dados')

        usuario = self.login.get()
        senha = self.senha.get()

        try:
            with conexao.cursor() as Cursor:
                Cursor.execute('select * from cadastros')
                resultados = Cursor.fetchall()
        
        except: 
            print('Erro ao fazer a consulta')

        for linha in resultados:
            if usuario == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                altenticado = True
                break
            else:
                altenticado = False

        if not altenticado:
            messagebox.showinfo('logim', 'Esmail ou senha invalido')

        if altenticado:
            self.root.destroy()
            if usuarioMaster:
                AdminJanela()

    def cadastrarBackAnd(self):
        codigoPadrao = '123#g'

        if self.codigoDeSeguranca.get() == codigoPadrao:
            if len(self.login.get()) <= 20:
                if len(self.senha.get()) <= 50:
                    nome = self.login.get()
                    senha = self.senha.get()
                            
                    try:
                        conexao = pymysql.connect(
                            
                            host='localhost', 
                            user='root',
                            password='',
                            db='erp',
                            charset='utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor
                        )

                    except:  
                        print('Erro ao conectar ao banco de dados')

                    try:
                        with conexao.cursor() as cursor:
                            cursor.execute('insert into cadastros (nome, senha, nivel) values (%s,%s ,%s)', (nome, senha, 1))
                            conexao.commit()
                        messagebox.showinfo('Cadastro', 'Usuário cadastrado com sucesso!')
                        self.root.destroy()

                    except:
                        print('Erro ao inserir dados')

                else:
                    messagebox.showinfo('Erro', 'Por favor insira uma senha de no maximo 50 caracteres')
            else:
                messagebox.showinfo('Erro', 'Por favor insira um usuario de no maximo 20 caracteres')
        else:
            messagebox.showinfo('Erro', 'Erro no código de segurança')

    def cadastro(self):
        self.root.geometry('270x150')
        Label(self.root,  text=('Chave de segurança')).grid(row=3, column=0, padx=5, pady=5)
        self.codigoDeSeguranca = Entry(self.root)
        self.codigoDeSeguranca.grid(row=3, column=1 , pady=5, padx=10)
        Button(self.root , text=('Cadastrar'), bg='#00BFFF', width=15, command=self.cadastrarBackAnd).grid(row=4, column=0, columnspan=3, pady=5, padx=10)

    def __init__(self):
        self.root = Tk()
        self.root.title('Login')
        self.root.resizable(False, False)
        self.root.geometry('250x140')
        Label(self.root, text='Faça login').grid(row=0, column=0, columnspan=2)
        
        Label(self.root, text='Usuario').grid(row=1, column=0)
        
        self.login = Entry(self.root)
        self.login.grid(row=1, column=1, padx=5, pady=5)

        Label(self.root, text='Senha').grid(row=2, column=0)
        
        self.senha = Entry(self.root, show='*')
        self.senha.grid(row=2, column=1, padx=5, pady=5)
        Button(self.root, text='login' , bg='green3',width=10, command=self.VerificaLogin).grid(row=5, column=0, padx=15, pady=15)

        Button(self.root, text='Cadastre-se' , bg='orange',width=10, command=self.cadastro).grid(row=5, column=1, padx=15, pady=15)


        self.root.mainloop()

JanelaLogin()