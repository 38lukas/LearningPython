# Life Tracker

A **Python desktop app** built with **PyQt6** for managing tasks, 
following the **MVC pattern**. Simple, clean, and extendable.

## Features

- Add, delete, and manage tasks  
- Toggle task status (`pending` ↔ `done`) with a double-click  
- Persistent storage in CSV  
- Enter key support for quick task input  
- Clean separation of **Model, View, Controller**  

## Tech Stack

- **Python 3.11+**  
- **PyQt6** for GUI  
- CSV for simple persistent storage  

## Quick Start

```bash
git clone https://github.com/your-username/life-tracker.git
cd life-tracker
pip install PyQt6
python app.py
```

## Project Structure
```bash
life_tracker/
│
├── app.py                 # Startpunkt der App
├── model.py               # Task-Datenmodell
├── storage.py             # CSV-Persistenz
│
├── controller/            # Alle Controller
│   ├── app_controller.py
│   ├── main_window_controller.py
│   └── detail_window_controller.py
│
├── ui/                    # Alle UI-Komponenten
│   ├── main_window.py
│   └── detail_window.py
│
└── data/
    └── tasks.csv          # Gespeicherte Tasks
```
