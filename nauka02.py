from tkinter import *

root = Tk()

# Tworzenie funkcji do przycisku
def myClick():
    myLabel = Label(root, text="Look I clicked a Button!!", fg="red")
    myLabel.pack()

# Lista funkcji ktore mozemy wykorzystac w przycisku
# padx=50 - zmienianie wysokości przycisku
# pady=50 - zmienianie szerokości przycisku
# state=DISABLED - wylaczenie przycisku (nie mozna go kliknąć)
# command=MyTest - przypisanie funkcji do przycisku
# fg="blue" - nadanie koloru tekstu
# bg="red" - nadanie tła przyciskowi, lub tekstu

# Tworzenie przycisków
myButton1 = Button(root, text="Click me!", padx=50, pady=50, command=myClick, fg="blue", bg="red")
myButton1.pack()

root.mainloop()
