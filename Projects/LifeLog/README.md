# LifeLog
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)

LifeLog is an app, which help you with task management, setting goals for yourself, and feeling like playing a game. 

---

## Features
- **Tasks**:
  - create/delete tasks
  - modify status, title, description
- **Two screens**:
  - MainWindow → task list
  - DetailWindow → task detail & editing
- **Saving & Loading**:
  - Automatic saving & loading of tasks (CSV file)
- **Clean structure**:
  - MVC (Model – View – Controller) + ApplicationManager

---

## Tech Stack

- Python 3.13
- PySide6 (GUI framework)
- Qt Designer

---

## Installation

1. Repository klonen
     ```bash
     git clone https://github.com/DEIN_USERNAME/LifeLog.git
     cd LifeLog
     ```

2. Abhängigkeiten installieren
  pip install -r requirements.txt
   ```bash
    pip install -r requirements.txt
   ```

3. Anwendung starten
   ```bash
    python src/life_log/app.py
   ```

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

## Contact

**Lukas Stieneke** – Data Scientist & Developer

- 📧 Email: lukas.stieneke@gmail.com
- 🐙 GitHub: [38lukas](https://github.com/38lukas)
- 💼 LinkedIn: [LinkedInName](https://linkedin.com/in/LinkedInName)
