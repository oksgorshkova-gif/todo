import time
from rich.console import Console 
from rich.panel import Panel       

console = Console()

class List:
    all_tasks = []

    def __init__(self):
        pass

    def add_task(self, task: dict) -> None:
        self.all_tasks.append(task)

    def list(self) -> None:
        self.show_tasks = []

        print("All tasks:")        
        for task in self.all_tasks:
            if task["completed"]:
                if task["description"]: 
                    self.show_tasks.append(f"- {task['title']} ([bold green]Completed[/bold green])\n  Description: {task['description']}") 
                else:
                    self.show_tasks.append(f"- {task['title']} ([bold green]Completed[/bold green])") 
            else:
                if task["description"]:
                    self.show_tasks.append(f"- {task['title']} ([bold yellow]Pending[/bold yellow])\n  Description: {task['description']}") 
                else:
                    self.show_tasks.append(f"- {task['title']} ([bold yellow]Pending[/bold yellow])")

        console.print(
            Panel.fit(
                "\n".join(self.show_tasks) if self.show_tasks else "[bold red]No tasks found.[/bold red]",
                border_style="blue",
            )
        )

class Logs:
    def __init__(self):
        self.events_log = []

    def log_event(self, event: str, *args) -> None:
        self.events_log.append((event, *args))

    def show_events(self) -> None:
        print("Events:")
        for event in self.events_log:
            if len(event) == 2:
                console.print(f"- [bold cyan]{event[0].upper()}[/bold cyan] task: [bold]{event[1]}[/bold]")
            elif len(event) == 3:
                action, title, status = event
                console.print(f"- [bold cyan]{action.upper()}[/bold cyan] task: [bold]{title}[/bold] - [red]{status}[/red]")
            elif event == "invalid_command" or event == "No_title_provided":
                console.print(f"- [bold red]{event}:[/bold red] {event[1]}") 

class ToDoApp:
    events_log = Logs().events_log
    tasks = List()

    def __init__(self):
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> list:
        return self.tasks

    def add_task(self, title: str, task_description: str = "") -> None:
        task = {
                "title": title,
                "description": task_description, 
                "completed": False, 
                "created_at": time.time(),
                "completed_at": None
                }

    def done(self, task_title: str) -> None:
        for task in self.tasks.all_tasks:
            if task["title"] == task_title:
                print(f"Completing task: {task_title}")
                task["completed"] = True
                task["completed_at"] = time.time()
                self.events_log.append(("complete", task_title))
                return  
        print(f"Task not found: {task_title}")
        self.events_log.append(("complete", task_title, "not found"))

    def delete(self, task_title: str) -> None:
        for i, task in enumerate(self.tasks.all_tasks):
            if task["title"] == task_title:
                del self.tasks.all_tasks[i]
                self.events_log.append(("delete", task_title))
                console.print(f"[green]Задача '{task_title}' удалена.[/green]")
                return
        print(f"Task not found: {task_title}")
        self.events_log.append(("delete", task_title, "not found"))

    def save_tasks(self) -> None:
        pass
            
    def help(self) -> None:
        print("Available commands:")
        print("- add: Add a new task with --title and optional --description")
        print("- done: Mark a task as completed with --title")
        print("- del: Delete a task with --title")
        print("- list: List all tasks")
        print("- events: Show task events")
        print("- help: Show this help message")
        
