import tkinter as tk

# --- Logik ---
def klick(zeichen):
    if zeichen == "=":
        try:
            ergebnis = eval(eingabe.get())
            eingabe.set(str(ergebnis))
        except:
            eingabe.set("Fehler")
    elif zeichen == "C":
        eingabe.set("")
    else:
        eingabe.set(eingabe.get() + zeichen)

# --- Fenster ---
fenster = tk.Tk()
fenster.title("Taschenrechner")
fenster.resizable(False, False)

eingabe = tk.StringVar()

# --- Anzeigefeld ---
anzeige = tk.Entry(fenster, textvariable=eingabe, font=("Arial", 24),
                   justify="right", bd=10, relief="sunken", width=16)
anzeige.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# --- Buttons ---
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

zeile = 1
spalte = 0

for b in buttons:
    farbe = "#f0a500" if b in "=/+-*" else "#e0e0e0"
    if b == "C":
        farbe = "#e05555"
    tk.Button(
        fenster, text=b, font=("Arial", 18),
        width=4, height=2, bg=farbe,
        command=lambda z=b: klick(z)
    ).grid(row=zeile, column=spalte, padx=5, pady=5)
    spalte += 1
    if spalte > 3:
        spalte = 0
        zeile += 1

fenster.mainloop()
