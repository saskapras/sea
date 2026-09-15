# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: SupportQueue
def report_summary(queue: dict) -> str:
    """Выводит отчёт по очереди: общее кол-во, по статусам и по приоритетам."""
    total = sum(len(queue.get(s, [])) for s in ('tickets', 'stats'))
    stats = queue.get('stats', {})
    parts = [f'Всего обращений: {total}']
    for status, tickets in stats.items():
        parts.append(f'  Статус "{status}": {len(tickets)}')
    return '\n'.join(parts)
