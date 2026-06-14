# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: SupportQueue
def edit_ticket(ticket_id: int, updates: dict) -> None:
    if ticket_id not in tickets:
        raise ValueError(f"Ticket {ticket_id} not found")
    
    for key, value in updates.items():
        if hasattr(tickets[ticket_id], key):
            setattr(tickets[ticket_id], key, value)

def delete_ticket(ticket_id: int) -> None:
    if ticket_id in tickets:
        del tickets[ticket_id]
