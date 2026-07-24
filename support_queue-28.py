# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: SupportQueue
def print_metrics(support_queue: dict) -> None:
    tickets = support_queue.get("tickets", [])
    if not tickets:
        print(f"Total tickets processed: 0")
        return

    total = len(tickets)
    open_tickets = sum(1 for t in tickets if t["status"] == "open")
    closed_tickets = sum(1 for t in tickets if t["status"] == "closed")
    avg_resolution_hours = (
        sum((t.get("resolved_at", 0) - t.get("created_at", 0)) / 3600.0 for t in tickets if t["status"] == "closed")
        / closed_tickets if closed_tickets else 0
    )

    high_priority_resolved = sum(1 for t in tickets if t["priority"] == "high" and t["status"] == "closed")
    sla_breached = sum(1 for t in tickets if t.get("sla_target_hours", 24) > 0 and (t.get("resolved_at", 0) - t.get("created_at", 0)) / 3600.0 > t["sla_target_hours"] and t["status"] == "closed")

    print(f"Total tickets processed: {total}")
    print(f"Open tickets: {open_tickets}")
    print(f"Closed tickets: {closed_tickets}")
    if closed_tickets:
        print(f"Avg resolution time: {avg_resolution_hours:.2f} hours")
    else:
        print("Avg resolution time: N/A (no closed tickets)")
    print(f"High priority resolved: {high_priority_resolved}")
    print(f"SLA breaches: {sla_breached}")
