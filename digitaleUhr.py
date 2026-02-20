import tkinter as tk
import time

root = tk.Tk()
root.title("Experimentelle Uhr")
root.geometry("325x100")

uhr_label = tk.Label(root, font=("Helvetica", 64), background="lightgrey", foreground="green", borderwidth="200")

def uhrzeit():
    aktuelle_uhrzeit = time.strftime("%H:%M:%S")
    uhr_label.config(text=aktuelle_uhrzeit)
    uhr_label.after(1000, uhrzeit)

uhr_label.pack(anchor="center")
uhrzeit()

root.mainloop()
