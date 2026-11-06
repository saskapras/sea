# === Stage 58: Добавь простую систему пользовательских представлений списка ===
# Project: SupportQueue
def get_ticket_view(queue, ticket, view):
    if view == "short":
        return f"[#{ticket['id']}] {ticket['subject']} | {ticket['status']} | {ticket['priority']}"
    elif view == "full":
        detail = "\n".join(f"  - {k}: {v}" for k, v in list(ticket.items()) if k not in ("id", "status", "priority"))
        return f"[#{ticket['id']}] {ticket['subject']}\n{detail}"
    elif view == "sla":
        opened = ticket.get("opened_at", "")
        sla = ticket.get("sla_hours", 24)
        elapsed = 0
        try:
            elapsed = (datetime.datetime.now() - datetime.datetime.fromisoformat(opened)).total_seconds() / 3600
        except Exception:
            pass
        remaining = max(0, sla - elapsed)
        status = "OK" if remaining >= 0 else "BREACH"
        return f"[#{ticket['id']}] {ticket['subject']} | SLA: {remaining:.1f}ч | {status}"
    return None


def print_queue_view(queue, tickets, view):
    if view not in ("short", "full", "sla"):
        return
    print(f"=== Список обращений ({view}) ===")
    for t in tickets:
        line = get_ticket_view(queue, t, view)
        if line:
            print(line)
    print("=== Конец списка ===")
