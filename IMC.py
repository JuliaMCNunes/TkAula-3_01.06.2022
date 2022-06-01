from tkinter import *


def imc1():
    tex6['text'] = 'Seu IMC é: '
    if entrada1.get().replace('.', '', 1).isnumeric() and entrada2.get().replace('.', '', 1).isnumeric():
        tex2['text'] = round(float(entrada1.get()) / float(entrada2.get()) ** 2, 1)
        if tex2['text'] < 18.5:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Abaixo do peso.'
            tex3['bg'] = '#ffad33'
        elif 18.5 < tex2['text'] < 25:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Peso ideal.'
            tex3['bg'] = '#66b3ff'
        elif 25 < tex2['text'] < 30:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Acima do peso.'
            tex3['bg'] = '#5cd65c'
        elif 30 < tex2['text'] < 35:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Obesidade Grau I.'
            tex3['bg'] = '#d9d926'
        elif 35 < tex2['text'] < 40:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Obesidade Grau II.'
            tex3['bg'] = '#ff8533'
        elif tex2['text'] >= 40:
            tex7['text'] = 'Classificação:'
            tex3['text'] = 'Obesidade Grau III.'
            tex3['bg'] = '#ff4d4d'
        else:
            pass
    else:
        tex3['text'] = 'Valor invalido!'


imc = Tk()
imc.geometry('300x200+800+260')
imc.config(background='#e6ccff')
imc.bind('<Return>', lambda event: imc1())

entrada1 = Entry(imc)
entrada2 = Entry(imc)
bot = Button(imc, text='Calcular', font='Arial 11', command=imc1, bg='#ffccdd')
tex1 = Label(imc, text='Calculando IMC', font='Arial 11', bg='#e6ccff')
tex2 = Label(imc, text='', font='Arial 11', bg='#e6ccff')
tex3 = Label(imc, text='', font='Arial 11', bg='#e6ccff')
tex4 = Label(imc, text='Peso:', font='Arial 11', bg='#e6ccff')
tex5 = Label(imc, text='Altura:', font='Arial 11', bg='#e6ccff')
tex6 = Label(imc, text='', font='Arial 11', bg='#e6ccff')
tex7 = Label(imc, text='', font='Arial 11', bg='#e6ccff')

tex1.place(x=100, y=10)
tex4.place(x=10, y=40)
tex5.place(x=10, y=60)
entrada1.place(x=60, y=40)
entrada2.place(x=60, y=60)
bot.place(x=120, y=90)
tex6.place(x=10, y=135)
tex2.place(x=90, y=135)
tex7.place(x=10, y=160)
tex3.place(x=110, y=160)

imc.mainloop()
