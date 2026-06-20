# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: SupportQueue
def sort_tickets(tickets, key='date'):
    priority_map = {'high': 0, 'medium': 1, 'low': 2}
    date_key = lambda t: (t.get('created_at') or '').replace('-', '') if isinstance(t.get('created_at'), str) else float('-inf')
    name_key = lambda t: t.get('subject', '').lower()
    
    sort_keys = {
        'date': (lambda x: -int(x.replace('-', '')) if x and '-' in x else 0),
        'priority': priority_map,
        'name': str
    }
    
    key_func = sort_keys.get(key, sort_keys['date'])
    return sorted(tickets, key=lambda t: (key_func(t) is not None, -priority_map.get(priority_key := next((k for k in ['high', 'medium', 'low'] if k in str(t).lower()), 2), priority_map['medium']), name_key(t)))
