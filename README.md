# ToDo CLI App

A simple command-line task manager built with Python.
The project demonstrates working with CLI interfaces, argument parsing, and persistent data storage.

---

## Features

* Add tasks
* Complete tasks
* Delete tasks
* List all tasks
* Track task events
* Formatted terminal output using `rich`

---

## Tech Stack

* Python 3
* argparse
* rich
* JSON

---

## Installation

```bash
git clone https://github.com/your-username/todo-cli-app.git
cd todo-cli-app
pip install rich
```

---

## Usage

```bash
python3 todo.py [action] [options]
```

---

## Commands

### Add a task

```bash
python3 todo.py add --title "Buy milk" --description "2L"
```

---

### Complete a task

```bash
python3 todo.py complete --title "Buy milk"
```

---

### Delete a task

```bash
python3 todo.py delete --title "Buy milk"
```

---

### List all tasks

```bash
python3 todo.py list
```

---

### Show events

```bash
python3 todo.py events
```

---

## Project Structure

```
.
├── todo.py          # CLI interface
├── models.py       # business logic
├── tasks.json      # data storage
└── README.md
```

---

## Architecture

The project is organized into three main layers:

* CLI layer (`todo.py`) — handles user input and command parsing
* Logic layer (`models.py`) — manages tasks and application logic
* Storage (`tasks.json`) — persists data between runs

---

## Notes

* Tasks are identified by title (no unique IDs implemented yet)
* Data is stored locally in a JSON file

---

## Future Improvements

* Add unique task identifiers
* Improve output formatting using `rich.Table`
* Implement filtering (completed / pending)
* Add search functionality
* Introduce a graphical interface (GUI)
* Add unit tests

---

## Author

Oksilition
