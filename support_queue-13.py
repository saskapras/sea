# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: SupportQueue
def search_tickets(query, fields=None):
    if not query:
        return tickets.copy()
    q = query.lower().strip()
    if fields is None:
        fields = ['id', 'subject', 'description']
    results = []
    for ticket in tickets:
        match = False
        for field_name in fields:
            value = ticket.get(field_name, '')
            if isinstance(value, str) and q in value.lower():
                match = True
                break
        if match:
            results.append(ticket.copy())
    return results
