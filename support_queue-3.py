# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: SupportQueue
class SupportQueue:
    def __init__(self):
        self.records = []
    
    def add_ticket(self, ticket_id, subject, priority, status='new', description='', sla_hours=24):
        record = {
            'id': ticket_id,
            'subject': subject,
            'priority': priority,
            'status': status,
            'description': description,
            'created_at': datetime.now(),
            'sla_deadline': datetime.now() + timedelta(hours=sla_hours),
            'responses': []
        }
        self.records.append(record)
        return record

    def update_status(self, ticket_id, new_status):
        for r in self.records:
            if r['id'] == ticket_id:
                r['status'] = new_status
                return True
        return False
    
    def get_ticket(self, ticket_id):
        for r in self.records:
            if r['id'] == ticket_id:
                return r.copy()
        return None

from datetime import datetime, timedelta
