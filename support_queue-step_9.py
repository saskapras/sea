# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: SupportQueue
import json, time
INITIAL_DATA = '''
{
    "tickets": [
        {"id": 1001, "subject": "Ошибка входа", "priority": "high", "status": "open", "created_at": "%Y-%m-%d %H:%M:%S"},
        {"id": 1002, "subject": "Вопрос по тарифу", "priority": "low", "status": "pending", "created_at": "%Y-%m-%d %H:%M:%S"}
    ],
    "sla_rules": [
        {"priority": "high", "hours": 4},
        {"priority": "medium", "hours": 24},
        {"priority": "low", "hours": 72}
    ]
}'''

def load_initial_data(data_string: str) -> dict:
    template = json.loads(INITIAL_DATA.replace("%Y-%m-%d %H:%M:%S", time.strftime("%Y-%m-%d %H:%M:%S")))
    return {k: v for k, v in template.items()}

if __name__ == "__main__":
    db = load_initial_data(INITIAL_DATA)
    print(f"Загружено {len(db['tickets'])} заявок.")
