# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: SupportQueue
def demo_run():
    print("=== Demo: SupportQueue ===")
    helpdesk = {
        "1": {"user": "Анна", "issue": "Не работает интернет", "priority": 3, "status": "new"},
        "2": {"user": "Борис", "issue": "Ошибка при печати", "priority": 1, "status": "in_progress"},
        "3": {"user": "Валентина", "issue": "Замена экрана ноутбука", "priority": 2, "status": "waiting"},
    }
    for t in ("new", "in_progress", "waiting"):
        print(f"--- Статус: {t} ---")
        for tid, ticket in helpdesk.items():
            if ticket["status"] == t:
                print(f"[{tid}] {ticket['user']}: {ticket['issue']} (приоритет {ticket['priority']})")

demo_run()
