from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('testowy pogram')
# Dodanie ikonki do programu
root.iconbitmap('c:/podajsciezke')

# Dodanie zdjecia do naszego programu
my_img = ImageTk.PhotoImage(Image.open("images/test.png"))
# wyswietlenie zdjecia za pomoca Label
my_label = Label(image=my_img)
my_label.pack()

# Przycisk ktory umożliwia wyłączyć program
button_exit = Button(root, text="Exit", command=root.quit)
button_exit.pack()


root.mainloop()