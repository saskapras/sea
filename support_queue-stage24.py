# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: SupportQueue
def print_ticket(ticket: Dict) -> None:
    """Compact one-ticket view."""
    t = ticket["ticket"]
    header = f"[#{t['id']}] {t['subject']} — {t['priority'].name} · {t['status'].name}"
    if t.get("sla"):
        sla = t["sla"]
        remaining = (sla.deadline - datetime.now(tz=timezone.utc)).total_seconds() / 3600
        marker = "⚠️" if remaining < 1 else "✅"
        header += f" · SLA {marker} ({remaining:.1f}h)"
    print(header)
    for key, val in t.items():
        if key not in ("id", "subject", "priority", "status", "sla"):
            print(f"  {key}: {val}")
