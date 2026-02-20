import tkinter as tk

root = tk.Tk()
root.title("IT Marv's Benutzeroberfläche")
root.geometry("300x200")
root.minsize(300, 200)

label = tk.Label(root, text="Wie heisst du?")
label.pack(pady=20)

entry = tk.Entry(root)
entry.pack()

def begruessung():
    name = entry.get()
    label.config(text=f"Hallo, {name}!")
    print("--- Name geändert ---")

button = tk.Button(root, text="Sag 'Hallo'", command=begruessung)
button.pack(pady=10)

button2 = tk.Button(root, text="Sag 'Auf Wiedersehen'", command=root.destroy)
button2.pack(pady = 20)  

root.mainloop()

print("--- Hauptfenster geschlossen ---")

print("--- Beendet ---")

