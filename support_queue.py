# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: SupportQueue
import time
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional, List, Dict

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

class TicketStatus(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"

class SupportTicket:
    def __init__(self, ticket_id: int, subject: str, description: str, priority: Priority):
        self.id = ticket_id
        self.subject = subject
        self.description = description
        self.priority = priority
        self.status = TicketStatus.OPEN
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.response_time_sla: Optional[datetime] = None

    def set_response_deadline(self, hours: int):
        if self.priority == Priority.LOW:
            self.response_time_sla = self.created_at + timedelta(hours=24)
        elif self.priority == Priority.MEDIUM:
            self.response_time_sla = self.created_at + timedelta(hours=12)
        else:
            self.response_time_sla = self.created_at + timedelta(hours=4)

    def update_status(self, new_status: TicketStatus):
        self.status = new_status
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[#{self.id}] {self.subject} | P:{self.priority.name} | S:{self.status.value}"

class SupportQueue:
    def __init__(self):
        self.tickets: List[SupportTicket] = []
        self.next_id = 1

    def add_ticket(self, subject: str, description: str, priority: Priority) -> SupportTicket:
        ticket = SupportTicket(self.next_id, subject, description, priority)
        ticket.set_response_deadline(0)
        self.tickets.append(ticket)
        self.next_id += 1
        return ticket

    def get_overdue_tickets(self) -> List[SupportTicket]:
        now = datetime.now()
        return [t for t in self.tickets if t.status == TicketStatus.OPEN and t.response_time_sla and now > t.response_time_sla]

# --- Демонстрационные данные и точка входа ---

if __name__ == "__main__":
    queue = SupportQueue()

    # Добавление демо-тикетов
    queue.add_ticket("Ошибка входа в систему", "Не могу войти по паролю", Priority.CRITICAL)
    queue.add_ticket("Вопрос по тарифам", "Как обновить подписку?", Priority.LOW)
    queue.add_ticket("Сбой отправки письма", "Письма не уходят клиентам", Priority.HIGH)

    # Вывод списка всех тикетов
    print("--- Текущие обращения ---")
    for ticket in queue.tickets:
        print(ticket)

    # Проверка просроченных (для демо просто покажем, что функция работает)
    print("\n--- Просроченные тикеты (демо) ---")
    overdue = queue.get_overdue_tickets()
