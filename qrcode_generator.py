from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=6)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image = image)
    image_label.image = image
    canvas.create_window(250, 450, window=image_label)

canvas = Canvas(root, width=500, height=600)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg="blue", font=("Arial", 30))
canvas.create_window(250, 50, window=app_label)

name_label = Label(root, text="Link name")
canvas.create_window(250, 100, window= name_label)

link_label = Label(root, text="Link")
canvas.create_window(250, 160, window=link_label)

name_entry = Entry(root)
canvas.create_window(250, 120, window= name_entry)

link_entry = Entry(root)
canvas.create_window(250, 180, window=link_entry, width=200)

button = Button(text= "Generate QR Code", command=generate)
canvas.create_window(250, 230, window=button)

root.mainloop()
