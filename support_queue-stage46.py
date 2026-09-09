# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: SupportQueue
def migrate_to_v2(data):
    """Миграция: добавляем поля 'priority' и 'sla_deadline' в каждый тикет."""
    new_data = {}
    for key, ticket in data.items():
        new_data[key] = {
            "id": ticket.get("id", key),
            "subject": ticket.get("subject", ""),
            "description": ticket.get("description", ""),
            "status": ticket.get("status", "open"),
            "priority": ticket.get("priority", "medium"),
            "sla_deadline": ticket.get("sla_deadline", None),
            "created_at": ticket.get("created_at", None),
            "updated_at": ticket.get("updated_at", None),
            "comments": ticket.get("comments", []),
        }
    return new_data
