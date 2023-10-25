from tkinter import *

root = Tk()

myLabel = Label(root, text="What's your name?", fg="Red")
myLabel.pack()

# stworzenie pustego pola do wpisania rzeczy (mozemy tam umieścić parametry)
e = Entry(root, borderwidth=5)
e.pack()
# e.insert(0, "What's your name:") - mozemy zrobic w pustym polu tekst
# e.get() - pobiera wszystko co wpisałeś

def myClick():
    hello = "hello", e.get()
    myLabel2 = Label(root, text=hello)
    myLabel2.pack()

myButton = Button(root, text="Click Me!", fg="blue", command=myClick)
myButton.pack()

root.mainloop()