import shlex

from models import Task, TaskManager
import view


def parse_args(raw: str) -> tuple[str, dict[str, str]]:
    parts = shlex.split(raw)
    if not parts:
        return "", {}

    action = parts[0].lower()
    kwargs: dict[str, str] = {}
    i = 1
    while i < len(parts):
        if parts[i].startswith("--") and i + 1 < len(parts):
            kwargs[parts[i][2:]] = parts[i + 1]
            i += 2
        else:
            i += 1
    return action, kwargs


def main() -> None:
    app = TaskManager()

    while True:
        try:
            raw = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not raw:
            continue

        action, kwargs = parse_args(raw)

        if action == "exit":
            view.show_success("Bye!")
            break

        elif action == "add":
            title = kwargs.get("title")
            if not title:
                view.show_error("--title is required.")
                continue
            result = app.add(title, kwargs.get("description", ""))
            if isinstance(result, Task):
                view.show_success(f"Task '{title}' added.")
            else:
                view.show_error(result)

        elif action == "done":
            title = kwargs.get("title")
            if not title:
                view.show_error("--title is required.")
                continue
            result = app.done(title)
            if isinstance(result, Task):
                view.show_success(f"Task '{title}' completed.")
            else:
                view.show_error(result)

        elif action == "del":
            title = kwargs.get("title")
            if not title:
                view.show_error("--title is required.")
                continue
            result = app.delete(title)
            if isinstance(result, Task):
                view.show_success(f"Task '{title}' deleted.")
            else:
                view.show_error(result)

        elif action == "list":
            view.show_tasks(app.tasks)

        elif action == "logs":
            view.show_events(app.events)

        elif action == "help":
            view.show_help()

        else:
            view.show_error(f"Unknown command: '{action}'. Type 'help' for usage.")


if __name__ == "__main__":
    main()
