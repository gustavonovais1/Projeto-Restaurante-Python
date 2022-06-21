from re import I
from tkinter import *

def calcular():
    pesso1 = float(peso.get())
    altura1 = float(altura.get())

    imc = pesso1/altura1 ** 2
    resposta['text'] = imc

    if imc >= 20:
        Label(janela, text='Ideal').grid(row=4, column=0)
    else:
        Label(janela, text='imc abixo').grid(row=4, column=0)

janela =  Tk()

janela.title('Teste')
janela.geometry('250x150')

Label(janela, text='Calcule o imc').grid(row=0, column=0, columnspan=2)
Label(janela, text='Digite o seu peso').grid(row=1, column=0)

peso = Entry(janela)
peso.grid(row=1, column=1)

Label(janela, text='Digite a sua altura').grid(row=2, column=0)

altura = Entry(janela)
altura.grid(row=2, column=1)

Button(janela, text='Calcular', command=calcular).grid(row=3, column=0)

resposta = Label(janela, text='Resposta')
resposta.grid(row=3, column=1)

janela.mainloop()

