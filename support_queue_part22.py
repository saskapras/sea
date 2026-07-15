# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: SupportQueue
def check_overdue_reminders(queue: list[dict]) -> list[dict]:
    overdue = []
    for ticket in queue:
        if ticket.get("status") != "pending":
            continue
        sla_hours = ticket.get("sla", {}).get("response_hours", 24)
        created_at = ticket.get("created_at", "").replace("T", " ").split()[0]
        now = datetime.now().strftime("%Y-%m-%d")
        if now > created_at:
            overdue.append({
                **ticket,
                "overdue": True,
                "days_overdue": (now - created_at).days,
            })
    return overdue
