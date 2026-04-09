from models import ToDoApp, List, Logs
import argparse
from rich.console import Console

console = Console()

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Простой CLI для управления задачами ToDo."
    )
    parser.add_argument(
        "action",
        choices=["add", "done", "del", "list", "logs", "help"],
        help="Действие для выполнения: add, done, del, list, logs, help",
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
    app = ToDoApp()
    list_app = List()
    logs = Logs()

    while True:
        command = input("Введите команду (add, done, del, list, logs, help) или 'exit' для выхода: ").strip()
        if command.lower() == "exit":
            console.print("[green]Выход из приложения.[/green]")
            break
        try:
            args = parser.parse_args(command.split())
        except SystemExit:
            console.print("[red]Неверная команда. Введите 'help' для получения списка доступных команд.[/red]")
            logs.log_event("invalid_command", command)
            continue

        if args.action == "add":
            if not args.title:
                console.print("[red]Ошибка: --title требуется для добавления задачи.[/red]")
                logs.log_event("No_title_provided", command)
                continue
            
            if args.title in list_app.all_tasks:
                console.print(f"[yellow]Задача '{args.title}' уже существует. Пропуск добавления.[/yellow]")
                logs.log_event("add", args.title, "already exists")
                continue

            app.add_task(args.title, args.description)
            # app.save_tasks() # Отключено сохранение в файл для упрощения тестирования
            logs.log_event("add", args.title, args.description)
            console.print(f"[green]Задача '{args.title}' добавлена.[/green]")              

        elif args.action == "done":
            if not args.title: 
                console.print("[red]Ошибка: --title требуется для завершения задачи.[/red]")
                logs.log_event("No_title_provided", command)
                continue

            app.done(args.title)
            app.save_tasks() # Отключено сохранение в файл для упрощения тестирования
            logs.log_event("done", args.title)
            console.print(f"[green]Задача '{args.title}' завершена.[/green]")

        elif args.action == "del":
            if not args.title:
                console.print("[red]Ошибка: --title требуется для удаления задачи.[/red]")
                logs.log_event("No_title_provided", command)
                continue    
            
            app.delete(args.title)
            #app.save_tasks() # Отключено сохранение в файл для упрощения тестирования
            logs.log_event("delete", args.title)

        elif args.action == "list":
            logs.log_event("List_requested", "list")
            list_app.list()

        elif args.action == "logs":
            logs.show_events()

        elif args.action == "help":
            logs.log_event("Help_requested", "help")
            app.help()

if __name__ == "__main__":
    main()
