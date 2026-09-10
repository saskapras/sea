# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: SupportQueue
def demo():
    q = SupportQueue()
    q.add_ticket("1001", "Кнопка не работает", "high", "open")
    q.add_ticket("1002", "Ошибка при оплате", "critical", "open")
    q.add_ticket("1003", "Вопрос по тарифу", "low", "open")

    q.add_agent("Анна", "open", "high")
    q.add_agent("Борис", "open", "critical")

    q.update_status("1001", "in_progress")
    q.update_status("1002", "in_progress")
    q.update_status("1003", "in_progress")

    q.add_response("1001", "Проверим в течение часа", "Анна")
    q.add_response("1002", "Менеджер уже на связи", "Борис")

    q.update_status("1001", "resolved")
    q.update_status("1002", "resolved")
    q.update_status("1003", "closed")

    print("=== Отчёт по завершённым обращениям ===")
    print(f"Решено: {q.get_resolved_count()}")
    print(f"Закрыто: {q.get_closed_count()}")
    print(f"Осталось: {q.get_open_count()}")
    print(f"В процессе: {q.get_in_progress_count()}")
    print(f"SLA-нарушения: {q.get_sla_violations()}")
