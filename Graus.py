from tkinter import *


def transfor():
    if entrada1.get().replace('.', '', 1).isnumeric():
        tex4['text'] = float(entrada1.get()) * 1.8 + 32


graus = Tk()
graus.geometry('300x200+800+260')
graus.config(background='#ccffe6')
graus.bind('<Return>', lambda event: transfor())

entrada1 = Entry(graus)
bot = Button(graus, text='Converter', font='Arial 11', command=transfor)
tex1 = Label(graus, text='Convertendo Valores', font='Arial 11', bg='#ccffe6')
tex2 = Label(graus, text='Graus Celsius: ', font='Arial 11', bg='#ccffe6')
tex3 = Label(graus, text='Graus Fahrenheit: ', font='Arial 11', bg='#ccffe6')
tex4 = Label(graus, text='', font='Arial 11', bg='#ccffe6')

tex1.place(x=80, y=10)
tex2.place(x=10, y=40)
entrada1.place(x=120, y=40)
tex3.place(x=10, y=70)
tex4.place(x=150, y=70)
bot.place(x=110, y=120)

graus.mainloop()
