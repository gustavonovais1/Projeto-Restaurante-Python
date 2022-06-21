from tkinter import *
from turtle import color

janela = Tk()
janela.title('Teste4')
janela.geometry('500x500')

frame = Frame(janela, width=300, height=300, bg='#C0C0C0').grid(row=0, column=0)
Label(frame, text='Teste de frame').grid(row=0, column=0)

janela.mainloop()