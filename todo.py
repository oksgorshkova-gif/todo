from models import ToDoApp
import argparse
from rich.console import Console
from rich.panel import Panel

console = Console()

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Простой CLI для управления задачами ToDo."
    )
    parser.add_argument(
        "action",
        choices=["add", "done", "del", "list", "events", "help"],
        help="Действие для выполнения: add, done, del, list, events, help",
    )
    parser.add_argument(
        "--title",
        help="Название задачи (требуется для add, done, del)",
    )
    parser.add_argument(
        "--description",
        default="",
        help="Описание задачи (только для add)",
    )
    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    app = ToDoApp()

    if args.action == "add":
        if not args.title:
            console.print("[red]Ошибка: --title требуется для добавления задачи.[/red]")
            return
        app.add_task(args.title, args.description)
        app.save_tasks()
        console.print(f"[green]Задача '{args.title}' добавлена.[/green]")

    elif args.action == "done":
        if not args.title:
            console.print("[red]Ошибка: --title требуется для завершения задачи.[/red]")
            return
        app.done(args.title)
        app.save_tasks()
        console.print(f"[green]Задача '{args.title}' завершена.[/green]")

    elif args.action == "del":
        if not args.title:
            console.print("[red]Ошибка: --title требуется для удаления задачи.[/red]")
            return
        app.delete(args.title)
        app.save_tasks()
        console.print(f"[green]Задача '{args.title}' удалена.[/green]")

    elif args.action == "list":
        app.list()

    elif args.action == "events":
        app.events()

    elif args.action == "help":
        app.help()

if __name__ == "__main__":
    main()
