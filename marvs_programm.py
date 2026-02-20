import tkinter
from tkinter.constants import *
root = tkinter.Tk()

root.title("GUI!")      # Titel in Leiste
# root.geometry("900x550")
root.minsize(width=1000, height=200)
root.maxsize()

frame = tkinter.Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

label = tkinter.Label(frame, background="black", foreground="green", font='Roboto 64 bold', text="Hallo, mein Herr. \nMarv's Programm")
label.pack(fill=X, expand=1, pady=20)

button = tkinter.Button(frame,text="Beende den Albtraum",command=root.destroy)
button.pack(side=BOTTOM)

root.mainloop()
