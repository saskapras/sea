# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: SupportQueue
import datetime

class AuditLog:
    def __init__(self):
        self.entries = []

    def record(self, table, record_id, action, **changes):
        entry = {
            'timestamp': datetime.datetime.now(),
            'table': table,
            'record_id': record_id,
            'action': action,
            'changes': changes
        }
        self.entries.append(entry)

    def get(self, table=None, record_id=None):
        filtered = self.entries
        if table:
            filtered = [e for e in filtered if e['table'] == table]
        if record_id is not None:
            filtered = [e for e in filtered if e['record_id'] == record_id]
        return filtered

    def get_latest(self, table=None, record_id=None):
        filtered = self.get(table, record_id)
        return filtered[-1] if filtered else None

    def clear(self):
        self.entries.clear()
