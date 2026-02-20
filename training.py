import tkinter as tk    # Tkinter importieren und Alias geben
# tkinter._test()       # Tkinter testen

root = tk.Tk()          # Tkinter zuweisen
root.title("Installation Marv-Programm") # Titel in der Leiste
# root.geometry("910x100") # Fenstergröße
root.minsize(width=910, height=70)
root.maxsize(width=950, height=80)

label1 = tk.Label(root, font='Roboto 42 bold', text="Willkommen beim Test-Programm", background="black", foreground="green") # Label Design
label1.pack()

root.mainloop()

print("Beendet")




# Weiterarbeiten mit YouTube Video: https://www.youtube.com/watch?v=oWrJD74KixA