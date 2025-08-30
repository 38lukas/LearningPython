# Life Tracker 

Ein einfaches **To-Do / Life-Tracking Tool** mit **Python + PyQt6**, um Aufgaben zu verwalten.  
Dieses Projekt ist als Lernprojekt für **Python, OOP, GUI-Programmierung und Software-Architektur** entstanden.

---

##  Features

- Aufgaben anlegen, bearbeiten und löschen
- Status verwalten: _offen_, _in Arbeit_, _erledigt_
- Aufgabenliste speichern & laden (JSON-Datei in `data/tasks.json`)
- GUI mit **PyQt6** (MainWindow, Buttons, Liste)
- Saubere Architektur:
  - `model.py` → Kernlogik (Task, TaskManager)
  - `storage.py` → Laden/Speichern
  - `ui/` → GUI-Komponenten (MainWindow, später Dialoge & Widgets)
  - `app.py` → Einstiegspunkt
  - `utils.py` → Hilfsfunktionen

---

## Projektstruktur

```text
life-tracker/
├─ README.md
├─ requirements.txt
├─ data/
│  └─ tasks.json          # Aufgaben werden hier gespeichert (in .gitignore)
├─ src/
│  └─ life_tracker/
│     ├─ __init__.py
│     ├─ app.py           # Einstiegspunkt
│     ├─ model.py         # Task + TaskManager
│     ├─ storage.py       # JSON Speichern/Laden
│     ├─ utils.py         # kleine Helfer
│     └─ ui/
│        └─ main_window.py # GUI (PyQt6 MainWindow)
└─ tests/                 # (empfohlen) pytest Tests
