# wczytanie modulu tkinter
from tkinter import *

root = Tk()

# tworzymy tekst w aplikacji
myLabel1 = Label(root, text="Hello world!")#.grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Michal")#.grid(row=1, column=1)

# tworzenie ekranu do aplkiacji
#Mylabel1.pack()

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()