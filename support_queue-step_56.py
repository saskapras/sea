# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: SupportQueue
def bulk_update_tickets():
    """Массовое обновление выбранных обращений.

    Перебирает выбранные записи в интерфейсе и применяет к ним
    единый набор полей (статус, приоритет, ответ, SLA-метка).
    """
    selected = get_selected_tickets()
    if not selected:
        print("Ничего не выбрано для массового обновления.")
        return

    new_status = input("Новый статус (например, resolved): ")
    new_priority = input("Новый приоритет (low/medium/high): ")
    new_sla_hours = input("Новый SLA в часах (Enter для сохранения): ")

    answers = input("Массовый ответ (Enter для пропуска): ")
    answer_id = None
    if answers:
        answer_id = create_support_answer(selected[0]["id"], answers)

    for ticket in selected:
        if new_sla_hours:
            ticket["sla_hours"] = int(new_sla_hours)
        ticket["status"] = new_status
        ticket["priority"] = new_priority
        if answer_id is not None:
            ticket.setdefault("answer_id", answer_id)
        update_ticket(ticket["id"])

    print(f"Обновлено записей: {len(selected)}")
