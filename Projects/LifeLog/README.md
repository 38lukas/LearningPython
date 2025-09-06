# LifeLog
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Build](https://img.shields.io/github/actions/workflow/status/OWNER/REPO/ci.yml?branch=main)

**LifeLog** is an app that helps you manage tasks and set goals for yourself.

---

## Features
- **Tasks**
  - Create, edit, and delete tasks
  - Modify status, title, description, and due date
  - Automatic validation of empty fields (default values applied)
  - Sorting by status, title or due date
- **Screens**
  - **MainWindow** → Task list, sorting by status, title, or due date
  - **DetailWindow** → Task details, editing, and saving
  - **Task Creation Window** → Quickly add new tasks
- **Persistence**
  - Automatic saving & loading of tasks (CSV)
  - Supports simple import/export of tasks
- **Clean architecture**
  - MVC (Model–View–Controller) pattern
  - Central `ApplicationManager` for window and state management
- **UX improvements**
  - Info panel showing total tasks and completed tasks
  - Status color coding in task list for quick visualization

---

## Tech Stack

- Python 3.13
- PySide6 (GUI framework)
- Qt Designer
- CSV for lightweight persistence

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
LifeLog/
├── .env                          # Virtual environment root
├── data/
│   └── tasks.csv
└── src/
    └── life_log/
        ├── ui/
        │   ├── controller/
        │   │   ├── detail_window.py
        │   │   ├── detail_window_controller.py
        │   │   ├── main_window.py
        │   │   ├── main_window_controller.py
        │   │   ├── task_creation_window.py
        │   │   └── task_creation_window_controller.py
        │   ├── views/
        │   │   ├── detail_window.ui
        │   │   ├── main_window.ui
        │   │   ├── task_creation_window.ui
        │   │   ├── ui_detail_window.py
        │   │   ├── ui_main_window.py
        │   │   └── ui_task_creation_window.py
        ├   └── app_manager.py
        ├── __init__.py
        ├── app.py
        ├── constants.py
        ├── model.py
        └── storage.py
```

---

## Contact

**Lukas Stieneke** – Data Scientist & Developer

- 📧 Email: lukas.stieneke@gmail.com
- 🐙 GitHub: [38lukas](https://github.com/38lukas)
- 💼 LinkedIn: [LinkedInName](https://linkedin.com/in/LinkedInName)
