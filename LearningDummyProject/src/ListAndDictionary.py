aufgaben_liste = []   # Liste für alle Aufgaben

while True:
    process = input("1: Beenden\n2: Aufgabe eingeben\n")
    if process == "1":
        break

    titel = input("Aufgabe eingeben: ")

    status_eingabe = input("Status eingeben (offen/erledigt, optional): ").lower()

    # Standardwert setzen
    status = "offen"

    # Falls der Nutzer etwas gültiges eingibt, überschreiben
    if status_eingabe in ["offen", "erledigt"]:
        status = status_eingabe

    # Neues Dictionary erzeugen
    neue_aufgabe = {"titel": titel, "status": status}

    # Aufgabe in die Liste einfügen
    aufgaben_liste.append(neue_aufgabe)

# Am Ende: Ausgabe aller Aufgaben
print("Alle Aufgaben:")
for aufgabe in aufgaben_liste:
    print(aufgabe)
