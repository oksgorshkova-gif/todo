from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from models import Event, Task

console = Console()


def show_success(message: str) -> None:
    console.print(f"[green]{message}[/green]")


def show_error(message: str) -> None:
    console.print(f"[red]{message}[/red]")


def show_tasks(tasks: list[Task]) -> None:
    if not tasks:
        console.print(Panel.fit("[bold red]No tasks found.[/bold red]", border_style="blue"))
        return

    table = Table(border_style="blue")
    table.add_column("#", style="dim")
    table.add_column("Title", style="bold")
    table.add_column("Description")
    table.add_column("Status")

    for i, task in enumerate(tasks, 1):
        status = "[bold green]Completed[/bold green]" if task.completed else "[bold yellow]Pending[/bold yellow]"
        table.add_row(str(i), task.title, task.description or "-", status)

    console.print(table)


def show_events(events: list[Event]) -> None:
    if not events:
        console.print("[dim]No events.[/dim]")
        return

    for event in events:
        line = f"- [bold cyan]{event.action.upper()}[/bold cyan] {event.title}"
        if event.detail:
            line += f" [red]({event.detail})[/red]"
        console.print(line)


def show_help() -> None:
    console.print(Panel.fit(
        "add --title TITLE [--description DESC]  Add a task\n"
        "done --title TITLE                      Complete a task\n"
        "del --title TITLE                       Delete a task\n"
        "list                                    List all tasks\n"
        "logs                                    Show event log\n"
        "help                                    Show this message\n"
        "exit                                    Quit",
        title="Commands",
        border_style="blue",
    ))
