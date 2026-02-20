
# BEISPIEL Eventhandler: Button

from tkinter import *       # Funktionen der Benutzeroberfläche importieren


# INTERFACE
window = Tk()                   # GUI-Modul tkinter (Tk) wird Variable zugewiesen
window.title("Das Programm")    # GUI-Titel
window.geometry("1281x716")     # Fenster-Größe
window.minsize(550, 716)        # minimale Fenstergröße
window.config(bg="#000000")   # in der config Hintergrund Farbe(background) festgelegt 


# CANVAS Hintergrund
canvas = Canvas(window, bg="#680081", width=1281, height=716, bd=1, highlightthickness=0, highlightcolor="#680081", highlightbackground="#680081")
canvas.pack(fill="none", expand=True)               # Bild zentrieren

# Bild einfügen
bg_image = PhotoImage(file="./hintergrund.png")
canvas.create_image(0, 0, image=bg_image, anchor=NW)


# MENÜ-FRAME
menu_frame = Frame(window, bg="#00FF00")
menu_frame.place(x=50, y=300)


# === Titel ===
titel = Label(
      menu_frame,
      text="MENÜ",
      font=("Roboto", 20, "bold"),
      fg="white",
      bg="#0000FF"
)
titel.pack(pady=(0, 20))

# === Label ===
output = Label(
      menu_frame,
      text="",
      fg="white",
      bg="#0000ff"
)
output.pack(pady=10)


# FUNKTIONEN
def start():
      output.config(text="Spiel gestartet")

def optionen():
      output.config(text="Optionen geöffnet")

def beenden():
      window.destroy()


# BUTTONS
btn_style = {
     "width": 20,
     "font": ("Roboto", 12),
     "bg": "#0000EE",
     "fg": "white",
     "activebackground": "#444444",
     "activeforeground": "white",
     "bd": 1
}

Button(menu_frame, text="Start", command=start, **btn_style).pack(pady=5)         #***********************************
Button(menu_frame, text="Optionen", command=optionen, **btn_style).pack(pady=5)
Button(menu_frame, text="Beenden", command=beenden, **btn_style).pack(pady=5)




# WIDGETS über dem Bild
canvas.create_text(150, 50, text="Das Programm", fill="white", font=("Robots", 24))

# FUNKTIONEN
def text_anzeigen(): # Funktion für Label
        lbl1.config(text = "Hier gibt es nichts zu sehen!") # Label erstellen
        lbl1.pack(pady=5)

def text_loeschen():
    lbl1.config(text="") # Label-Inhalt löschen
    lbl1.pack(pady=5)

# LABEL
lbl1 = Label(window, text="", bg="black", fg="white") # Titel
canvas.create_window(200, 150, window=lbl1)
lbl1.pack(pady=5)

# BUTTONS
btn1 = Button(window, text="Text anzeigen", command=text_anzeigen)
btn1.pack(pady=5)

btn2 = Button(window, text="Text löschen.", command=text_loeschen)
btn2.pack(pady=5)

canvas.create_window(240, 200, window=btn1)

canvas.create_window(240, 200, window=btn2)



window.mainloop()





# BUTTONS TK
# canvas.btn1 = Button(text="Willste einen Tipp?", width=15, height=1, background="#FED547", command=text) # Button erstellen - command ruft Funktion auf
# btn1.grid # 2. Zeile

# btn2 = Button(text="Keinen Tipp.", width=15, background="#0000FF", fg="white", command=textloeschen)
# btn2.grid

# btn3 = Button(text="")

# btnExit = Button(text = "Exit", width=10, background="red", fg="black", comman=window.destroy)
# btnExit.grid # 3. Zeile

# BUTTONS CANVAS
# button_top = btn1.Button(None, text="Button", bd=1, highlightthickness=0)
# canvas_top.create_window(20,20, window=button_top, anchor='nw')





###########################################################################

# import Tkinter as tk

# app_win = tk.Tk()

# back_gnd = tk.Canvas(app_win)
# back_gnd.pack(expand=True, fill='both')

# back_gnd_image = tk.PhotoImage(file="image.gif")
# back_gnd.create_image(0, 0, anchor='nw', image=back_gnd_image)

# button = tk.Button(None, text="Button", bd=1, highlightthickness=0)
# back_gnd.create_window(20,20, window=button, anchor='nw')

# app_win.mainloop()