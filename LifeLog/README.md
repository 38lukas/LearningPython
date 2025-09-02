# LifeLog – Simple Task Tracker

A small **task-tracking tool** built with PySide6 and QtCreator.

## Features
- Tasks with **title, status, and description**
- **Two screens**:
  - MainWindow → task list
  - DetailWindow → task detail & editing
- Status dropdown (`Pending / In Progress / Finished`)
- Automatic saving & loading of tasks (CSV file)
- **Clean structure**: MVC (Model – View – Controller) + ApplicationManager

---

## Tech Stack

- Python 3.11+
- PySide6 (GUI framework)

---

## Project Structure
```text
src/
├── data/
│   └── tasks.csv                  # CSV-Datei zur Speicherung der Aufgaben
├── life_log/
│   ├── ui/
│   │   ├── controller/
│   │   │   ├── detail_window.py
│   │   │   ├── detail_window_controller.py
│   │   │   ├── main_window.py
│   │   │   └── main_window_controller.py
│   │   └── views/
│   │       ├── detail_window.ui
│   │       ├── main_window.ui
│   │       ├── ui_detail_window.py
│   │       ├── ui_main_window.py
│   │       ├── app_manager.py
│   │       └── __init__.py
├── app.py                         # Einstiegspunkt der App
├── model.py                       # Task-Datenmodell
└── storage.py                     # CSV-Speicherung
```
---

