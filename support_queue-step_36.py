# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: SupportQueue
def repair_data():
    """Простая проверка целостности и ремонт базовых проблем."""
    issues = 0
    for ticket in tickets:
        if ticket.get("priority") not in ["low", "medium", "high", "urgent"]:
            ticket["priority"] = "medium"
            issues += 1
        if ticket.get("status") not in ["new", "in_progress", "resolved", "closed"]:
            ticket["status"] = "new"
            issues += 1
        if ticket.get("created_at") is None:
            ticket["created_at"] = datetime.datetime.now().isoformat()
            issues += 1
        if ticket.get("updated_at") is None:
            ticket["updated_at"] = datetime.datetime.now().isoformat()
            issues += 1
        if ticket.get("response_time") is None and ticket.get("status") == "resolved":
            ticket["response_time"] = datetime.datetime.now() - datetime.datetime.fromisoformat(ticket["created_at"])
            issues += 1
    return issues
