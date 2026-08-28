# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: SupportQueue
import unittest
from datetime import datetime, timedelta

class TestSupportQueueEdgeCases(unittest.TestCase):
    def setUp(self):
        from support_queue import SupportQueue, Ticket, Priority
        self.q = SupportQueue()

    def test_duplicate_ticket_id_rejected(self):
        t = Ticket("1", "t1", "P", "O", "Open", "2024-01-01", "2024-01-03")
        self.q.add(t)
        with self.assertRaises(ValueError):
            self.q.add(Ticket("1", "t1", "P", "O", "Open", "2024-01-01", "2024-01-03"))

    def test_close_opened_ticket_fails(self):
        t = Ticket("1", "t1", "P", "O", "Open", "2024-01-01", "2024-01-03")
        self.q.add(t)
        with self.assertRaises(ValueError):
            t.set_status("Closed")

    def test_close_already_closed_ticket_fails(self):
        t = Ticket("1", "t1", "P", "O", "Open", "2024-01-01", "2024-01-03")
        self.q.add(t)
        t.set_status("Closed")
        with self.assertRaises(ValueError):
            t.set_status("Closed")

    def test_answer_on_closed_ticket(self):
        t = Ticket("1", "t1", "P", "O", "Open", "2024-01-01", "2024-01-03")
        self.q.add(t)
        t.set_status("Closed")
        with self.assertRaises(ValueError):
            t.add_answer("A2")

    def test_sla_breach_open_ticket(self):
        t = Ticket("1", "t1", "P", "O", "Open", "2024-01-01", "2024-01-03")
        self.q.add(t)
        assert t.sla_breached(datetime(2024, 1, 4))
        assert not t.sla_breached(datetime(2024, 1, 2))

    def test_sla_breach_closed_ticket(self):
        t = Ticket("1", "t1", "P", "O", "Open", "2024-01-01", "2024-01-03")
        self.q.add(t)
        t.set_status("Closed")
        assert not t.sla_breached(datetime(2024, 1, 4))

    def test_empty_queue_length(self):
        self.assertEqual(len(self.q), 0)

    def test_queue_order_by_priority(self):
        self.q.add(Ticket("1", "t1", "P", "O", "Open", "2024-01-01", "2024-01-03"))
        self.q.add
