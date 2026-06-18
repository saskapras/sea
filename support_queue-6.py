# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: SupportQueue
def filter_tickets(status=None, category=None, tags=None):
    filtered = []
    for ticket in tickets:
        if status and ticket['status'] != status:
            continue
        if category and ticket.get('category') != category:
            continue
        if tags:
            ticket_tags = ticket.get('tags', [])
            if not any(tag in ticket_tags for tag in tags):
                continue
        filtered.append(ticket)
    return filtered

def get_ticket_summary():
    active_count = sum(1 for t in tickets if t['status'] == 'open')
    avg_priority = sum(t.get('priority', 0) for t in tickets) / max(len(tickets), 1)
    overdue_sla = [t for t in tickets if t['sla_deadline'] and datetime.datetime.now() > datetime.datetime.fromisoformat(t['sla_deadline'])]
    return {'active': active_count, 'avg_priority': round(avg_priority, 2), 'overdue_sla': len(overdue_sla)}
