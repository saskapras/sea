# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: SupportQueue
def generate_summary(queue_data):
    if not queue_data:
        return "Сводка данных пуста."
    
    total = len(queue_data)
    open_count = sum(1 for item in queue_data if item['status'] == 'open')
    closed_count = sum(1 for item in queue_data if item['status'] == 'closed')
    high_priority = sum(1 for item in queue_data if item.get('priority', 0) >= 3)
    
    sla_breached = [item for item in queue_data 
                     if item['status'] == 'open' and (item.get('created_at') or '')]
    
    avg_response_time = sum(item.get('response_hours', 0) for item in queue_data if item['status'] == 'closed') / closed_count if closed_count else 0
    
    return f"Всего обращений: {total}. Открыто: {open_count}, Закрыто: {closed_count}. " \
           f"Высокий приоритет: {high_priority}. Среднее время ответа (закрытые): {avg_response_time:.1f} ч."
