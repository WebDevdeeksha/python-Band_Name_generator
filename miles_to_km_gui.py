# Mile to Km conversion; Formula to calculate is to multiply the mile number with (1.609341666666667) float number
# I'm taking an accurate number 1.

from tkinter import *

root = Tk()
root.title("Mile to Km Converter")
root.minsize(width=600, height=200)
root.config(padx=100, pady=50, bg="black")

def mile_to_km():
    mile = float(mile_input.get())
    km = mile * 1.61
    km_input.config(text=f"{km}")

mile_input = Entry(root, font=("Arial", 16), fg="black", highlightthickness=1)
mile_input.grid(row=0, column=0)

mile = Label(root, text="Mile", font=("Arial", 16), fg="white", bg="black")
mile.grid(row=1, column=0)

button = Button(root, text="Calculate", font=("Arial", 14), fg="white", bg="black", command=mile_to_km, highlightcolor="black", highlightthickness=1)
button.grid(row=0, column=6, padx=10, pady=10)

km_input = Label(root, text=" 0 ", font=("Arial", 16), fg="black", bg="white", highlightthickness=1)
km_input.grid(row=0, column=12)

km = Label(root, text="Km", font=("Arial", 16), fg="white", bg="black")
km.grid(row=1, column=12)

root.mainloop()


