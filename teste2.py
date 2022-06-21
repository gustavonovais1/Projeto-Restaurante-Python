from cmath import tan
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import color

from matplotlib.pyplot import grid

janela =  Tk()

janela.title('Treeview')

tree = ttk.Treeview(janela, selectmode='browse',
column=('coluna1','coluna2', 'coluna3', 'coluna4'), show='headings') 

tree.column('coluna1', width=200, minwidth=50, stretch=NO)
tree.heading('#1', text='Nome')

tree.column('coluna2', width=200, minwidth=50, stretch=NO)
tree.heading('#2', text='idade')

tree.column('coluna3', width=200, minwidth=50, stretch=NO)
tree.heading('#3', text='Endereco')

tree.column('coluna4', width=100, minwidth=50, stretch=NO)
tree.heading('#4', text='ID')

elementos = ['ustavo', '13', 'Rua Emiliano Dias', '1']
for i in range(0, 4):
    tree.insert('', END, values=elementos, tag='1')

tree.grid(row=0, column=0)

janela.mainloop()