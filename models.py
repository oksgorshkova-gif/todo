import time
import json
import os
from rich.console import Console 
from rich.panel import Panel       

console = Console()

class ToDoApp:
    events_log = []

    def __init__(self):
        self.FILE_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "tasks.json"
        )
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> list:
        try:
            with open(self.FILE_PATH, "r", encoding="utf-8") as tasks_file:
                return json.load(tasks_file)
        except FileNotFoundError:
            return []

    def add_task(self, title: str, task_description: str = "") -> None:
        print(f"Adding task: {title}")
        task = {
                "title": title,
                "description": task_description, 
                "completed": False, 
                "created_at": time.time(),
                "completed_at": None
                }
        self.tasks.append(task)
        self.events_log.append(("add", title))

    def done(self, task_title: str) -> None:
        for task in self.tasks:
            if task["title"] == task_title:
                print(f"Completing task: {task_title}")
                task["completed"] = True
                task["completed_at"] = time.time()
                self.events_log.append(("complete", task_title))
                return  
        print(f"Task not found: {task_title}")
        self.events_log.append(("complete", task_title, "not found"))

    def delete(self, task_title: str) -> None:
        for i, task in enumerate(self.tasks):
            if task["title"] == task_title:
                print(f"Deleting task: {task_title}")
                del self.tasks[i]
                self.events_log.append(("delete", task_title))
                return
        print(f"Task not found: {task_title}")
        self.events_log.append(("delete", task_title, "not found"))

    def list(self) -> None:
        print("All tasks:")
        all_tasks = []
        for task in self.tasks:
            if task["completed"]:
                all_tasks.append(f"- {task['title']} ([bold green]Completed[/bold green])\n  Description: {task['description']}")  
            else:
                all_tasks.append(f"- {task['title']} ([bold yellow]Pending[/bold yellow])\n  Description: {task['description']}") 
       
        console.print(
            Panel.fit(
                "\n".join(all_tasks) if all_tasks else "[bold red]No tasks found.[/bold red]",
                border_style="blue",
            )
        )

    def save_tasks(self) -> None:
        with open(self.FILE_PATH, "w", encoding="utf-8") as tasks_file:
            json.dump(self.tasks, tasks_file, indent=4)

    def events(self) -> None:
        print("Task events:")
        for event in self.events_log:
            if len(event) == 2:
                action, title = event
                console.print(f"- [bold cyan]{action.upper()}[/bold cyan] task: [bold]{title}[/bold]")
            elif len(event) == 3:
                action, title, status = event
                console.print(f"- [bold cyan]{action.upper()}[/bold cyan] task: [bold]{title}[/bold] - [red]{status}[/red]")
    
    def help(self) -> None:
        print("Available commands:")
        print("- add: Add a new task")
        print("- done: Mark a task as completed")
        print("- del: Delete a task")
        print("- list: List all tasks")
        print("- events: Show task events")
        print("- save: Save tasks to file")
        print("- help: Show this help message")
        
