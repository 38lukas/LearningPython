import pandas as pd


CSV_PATH = "data/data.csv"


def main():

    while True:
        print("Willkommen zur To-Do Liste!\n")
        eingabe = input("1: Aufgabe hinzufügen\n" + "2: Aufgabe löschen\n" + "3: Aufgaben anzeigen\n" + "4: Beenden\n")

        match eingabe:
            case "1":
                neue_aufgabe = {"titel": input("Titel: "),
                                "status": input("Status: ")}

                aufgaben_df = auslesen()

                aufgaben_df = pd.concat([aufgaben_df, pd.DataFrame([neue_aufgabe])], ignore_index=True)
                speichern(aufgaben_df)

            case "2":
                pass
            case "3":
                aufgaben_df = auslesen()
                if not aufgaben_df.empty:

                    for i in range(0, len(aufgaben_df)):
                        zeile = aufgaben_df.iloc[i]
                        print(f"Titel: {zeile['titel']}\n" + f"Status: {zeile['status']}\n")

            case "4":
                print("Exiting Programm...")
                return
            case _:
                print("Wrong command!")


def auslesen():
    try:
        data_frame = pd.read_csv(CSV_PATH)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        print("Error: Datei ist leer!")
        return pd.DataFrame(columns=["titel", "status"])

    if data_frame.empty:
        print("Error: Datei ist leer!")
        return pd.DataFrame(columns=["titel", "status"])

    return data_frame

def speichern(data_frame: pd.DataFrame):
    data_frame.to_csv(CSV_PATH, index=False)
    print(data_frame)
    print("Erfolgreich gespeichert!")

main()