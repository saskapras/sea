# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: SupportQueue
import json, os, time

DATA_FILE = "support_queue.json"

def save_to_json(queue_data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(queue_data, f, ensure_ascii=False, indent=2)

def load_from_json():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Восстанавливаем типы данных при загрузке из JSON (строки вместо объектов)
            for ticket in data.get('tickets', []):
                if isinstance(ticket['created_at'], str):
                    ticket['created_at'] = time.mktime(time.strptime(ticket['created_at'], '%Y-%m-%d %H:%M:%S'))
                if 'sla_deadline' in ticket and isinstance(ticket['sla_deadline'], str):
                    ticket['sla_deadline'] = time.mktime(time.strptime(ticket['sla_deadline'], '%Y-%m-%d %H:%M:%S'))
            return data.get('tickets', [])
    except (json.JSONDecodeError, ValueError):
        return []

def init_storage():
    if not os.path.exists(DATA_FILE):
        save_to_json({'tickets': [], 'last_id': 0})
