# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: SupportQueue
class Ticket:
    def __init__(self, title: str, priority: int = 1, status: str = "open"):
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        if priority < 1 or priority > 5:
            raise ValueError("Priority must be between 1 and 5")
        valid_statuses = {"open", "in_progress", "resolved"}
        if status not in valid_statuses:
            raise ValueError(f"Status must be one of {valid_statuses}")
        self.title = title.strip()
        self.priority = priority
        self.status = status

def validate_input(title: str, priority: int, status: str) -> dict[str, bool]:
    errors = []
    if not isinstance(title, str):
        errors.append("Title must be a string")
    elif len(title.strip()) == 0:
        errors.append("Title cannot be empty")
    else:
        title = title.strip()

    if priority < 1 or priority > 5:
        errors.append("Priority must be between 1 and 5")

    valid_statuses = {"open", "in_progress", "resolved"}
    if status not in valid_statuses:
        errors.append(f"Status must be one of {valid_statuses}")

    return {"is_valid": len(errors) == 0, "errors": errors}
