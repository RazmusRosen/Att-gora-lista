import tkinter as tk
import json

def visa_att_gora_lista():
    top = tk.Tk()
    top.title("Att göra-lista")

    # Skapa en lista för att lagra Entry-widgetar och knappar
    rows = []

    def lagg_till_rad():
        nonlocal rows

        # Skapa en ny Label för rubriken
        label = tk.Label(top, text=f"Göra {len(rows) + 1}")
        label.pack()

        # Skapa ett nytt Entry-fält för den nya raden
        entry = tk.Entry(top, width=30)
        entry.pack()

        # Skapa en knapp för att ta bort raden
        remove_button = tk.Button(top, text="Ta bort", command=lambda current_row=len(rows): ta_bort_rad(rows, current_row))
        remove_button.pack()

        # Lägg till raden i listan
        rows.append((label, entry, remove_button))

        # Flytta knappen längst ner i rutan
        add_row_button.pack(side=tk.BOTTOM)

    # Läs in uppgifterna från filen om den finns
    inlasad_data = las_data_fran_fil()
    if inlasad_data:
        for rad in inlasad_data:
            label = tk.Label(top, text=rad["rubrik"])
            label.pack()

            entry = tk.Entry(top, width=30)
            entry.pack()
            entry.insert(tk.END, rad["innehall"])

            remove_button = tk.Button(top, text="Ta bort", command=lambda current_row=len(rows): ta_bort_rad(rows, current_row))
            remove_button.pack()

            rows.append((label, entry, remove_button))

    # Skapa en knapp för att spara listan
    save_button = tk.Button(top, text="Spara", command=lambda: spara_listan(rows))
    save_button.pack(side=tk.BOTTOM)

    # Skapa en knapp för att lägga till en ny rad
    add_row_button = tk.Button(top, text="Lägg till rad", command=lagg_till_rad)
    add_row_button.pack(side=tk.BOTTOM)

    top.mainloop()  # Starta huvudloopen för tkinter-applikationen

def spara_listan(rows):
    data = []

    # Hämta innehållet från Entry-widgetarna
    for i, (label, entry, _) in enumerate(rows, start=1):
        innehall = entry.get()
        data.append({"rubrik": label.cget("text"), "innehall": innehall})

    # Spara data till fil
    with open("att_gora.json", "w") as file:
        json.dump(data, file)

def las_data_fran_fil():
    try:
        with open("att_gora.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None

def ta_bort_rad(rows, current_row):
    label, entry, remove_button = rows[current_row]
    entry.destroy()
    label.destroy()
    remove_button.destroy()
    rows.pop(current_row)

    # Uppdatera rubrikerna för efterföljande rader
    for i in range(current_row, len(rows)):
        label, _, _ = rows[i]
        label.config(text=f"Göra {i+1}")


# Anropa funktionen för att visa "Att göra"-listan
visa_att_gora_lista()
