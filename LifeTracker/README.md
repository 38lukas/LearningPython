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
app.py              # Main controller
model.py            # Task model
storage.py          # CSV persistence
ui/main_window.py   # Window for task management
ui/detail_window.py # Window for task detail
data/tasks.csv      # Saved tasks
```