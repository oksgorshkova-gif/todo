from __future__ import annotations

from dataclasses import dataclass, field
from time import time
from uuid import uuid4


@dataclass
class Event:
    action: str
    title: str
    detail: str = ""
    timestamp: float = field(default_factory=time)


@dataclass
class Task:
    title: str
    description: str = ""
    completed: bool = False
    id: str = field(default_factory=lambda: uuid4().hex[:8])
    created_at: float = field(default_factory=time)
    completed_at: float | None = None


class TaskManager:
    def __init__(self):
        self._tasks: dict[str, Task] = {}
        self.events: list[Event] = []

    @property
    def tasks(self) -> list[Task]:
        return list(self._tasks.values())

    def find_task(self, title: str) -> Task | None:
        return self._tasks.get(title)

    def add(self, title: str, description: str = "") -> Task | str:
        if title in self._tasks:
            self._log("add", title, "already exists")
            return f"Task '{title}' already exists."
        task = Task(title=title, description=description)
        self._tasks[title] = task
        self._log("add", title)
        return task

    def done(self, title: str) -> Task | str:
        task = self._tasks.get(title)
        if not task:
            self._log("done", title, "not found")
            return f"Task not found: {title}"
        task.completed = True
        task.completed_at = time()
        self._log("done", title)
        return task

    def delete(self, title: str) -> Task | str:
        task = self._tasks.pop(title, None)
        if not task:
            self._log("delete", title, "not found")
            return f"Task not found: {title}"
        self._log("delete", title)
        return task

    def _log(self, action: str, title: str, detail: str = "") -> None:
        self.events.append(Event(action=action, title=title, detail=detail))
