# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: SupportQueue
import unittest
from datetime import datetime, timedelta

class TestSupportQueue(unittest.TestCase):
    def test_priority_order(self):
        q = SupportQueue()
        q.add_ticket("T001", "Critical", "User can't login", "Pending")
        q.add_ticket("T002", "Low", "UI typo", "Pending")
        q.add_ticket("T003", "High", "Data loss risk", "Pending")
        tickets = q.get_pending_tickets()
        self.assertEqual(tickets[0]["priority"], "Critical")
        self.assertEqual(tickets[1]["priority"], "High")
        self.assertEqual(tickets[2]["priority"], "Low")

    def test_status_update(self):
        q = SupportQueue()
        q.add_ticket("T001", "Normal", "Question", "Open")
        q.update_status("T001", "Answered")
        tickets = q.get_pending_tickets()
        self.assertEqual(tickets, [])
        answered = q.get_answered_tickets()
        self.assertEqual(len(answered), 1)
        self.assertEqual(answered[0]["status"], "Answered")

    def test_sla_check(self):
        q = SupportQueue()
        q.add_ticket("T001", "Normal", "Question", "Open", sla_minutes=60)
        q.add_ticket("T002", "Normal", "Question", "Open", sla_minutes=120)
        now = datetime.now()
        deadline1 = now - timedelta(minutes=10)
        deadline2 = now - timedelta(minutes=10)
        q.check_sla(deadline1)
        self.assertEqual(len(q.get_breached_tickets()), 1)
        self.assertEqual(q.get_breached_tickets()[0]["ticket_id"], "T001")
        q.check_sla(deadline2)
        self.assertEqual(len(q.get_breached_tickets()), 2)

    def test_ticket_search(self):
        q = SupportQueue()
        q.add_ticket("T001", "Normal", "Question about API", "Open")
        q.add_ticket("T002", "Normal", "Question about UI", "Open")
        q.add_ticket("T003", "Normal", "Question about API", "Open")
        results = q.search_tickets("API")
        self.assertEqual(len(results), 2)
        results = q.search_tickets("UI")
        self.assertEqual(len(results), 1)

if __name__ == "__main__":
    unittest.main()
