import csv
import pandas as pd

from src.ListAndDictionary import status

aufgaben = [
    {"titel": "Einkaufen", "status": "offen"},
    {"titel": "Python ueben", "status": "erledigt"},
    {"titel": "Lesen"}
]

def speichern():
    with open('../data/aufgaben.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["titel", "status"])
        writer.writeheader()
        for aufgabe in aufgaben:
            if not aufgabe.get("status"):
                aufgabe.setdefault("status", "offen")
        writer.writerows(aufgaben)

def einlesen():
    with open('../data/aufgaben.csv', 'r') as file:
        reader = csv.DictReader(file)
        aufgaben_geladen = list(reader)
        print(aufgaben_geladen)



speichern()
einlesen()



df = pd.read_csv('../data/aufgaben.csv')

neu = {"titel": "Sport machen", "status": "offen"}
df = pd.concat([df, pd.DataFrame([neu])], ignore_index=True)


print(df["status"].value_counts())


for i in range(0, df["titel"].count()):
    zeile = df.iloc[i]
    print(f"Titel: {zeile["titel"]}" + "\n" + f"Status: {zeile["status"]}" + "\n")