# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: SupportQueue
def delete_ticket(ticket_id: int) -> bool:
    if not isinstance(ticket_id, int):
        raise ValueError("ID должен быть целым числом")
    
    try:
        index = tickets.index({'id': ticket_id})
        deleted_ticket = tickets.pop(index)
        
        # Проверка на удаление по SLA (опционально, если нужно логировать)
        if 'sla_deadline' in deleted_ticket and deleted_ticket['status'] == 'open':
            print(f"Удалено обращение {deleted_ticket['id']} с истекшим SLA.")
        
        return True
    except ValueError:
        # Обработка отсутствующего идентификатора без выброса ошибки, если это не критично
        # Или можно вернуть False и записать в лог. Здесь возвращаем False для безопасности.
        print(f"Обращение с ID {ticket_id} не найдено или уже удалено.")
        return False

# Пример использования (раскомментируйте при тестировании):
# if __name__ == "__main__":
#     delete_ticket(1)  # Удаляет, если существует
#     delete_ticket(999) # Возвращает False
