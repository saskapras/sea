# === Stage 17: Добавь группировку записей по категориям ===
# Project: SupportQueue
def group_by_category(records):
    """Группирует записи по категории (поле category)."""
    grouped = {}
    for r in records:
        cat = r.get("category", "Uncategorized")
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(r)
    return grouped

def print_grouped(grouped):
    """Выводит сгруппированные записи."""
    for cat, records in sorted(grouped.items()):
        print(f"\n[{cat}] ({len(records)} шт.)")
        for r in records:
            status = r.get("status", "unknown")
            priority = r.get("priority", "?")
            title = r.get("title", "(без заголовка)")
            print(f"  • {priority} | {status}: {title}")

# Пример использования:
if __name__ == "__main__":
    sample_records = [
        {"category": "Billing", "priority": "high", "status": "open", "title": "Неверный счет"},
        {"category": "Technical", "priority": "medium", "status": "in_progress", "title": "Ошибка логина"},
        {"category": "Billing", "priority": "low", "status": "closed", "title": "Смена валюты"},
    ]
    grouped = group_by_category(sample_records)
    print_grouped(grouped)
