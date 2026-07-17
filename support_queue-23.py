# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: SupportQueue
def print_table(headers, rows):
    col_widths = [len(h) for h in headers] + [max(len(str(r[i])) if r else 0, len(headers[i])) for i in range(len(headers))]
    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
    print("\n".join([fmt.format(*headers), "-" * (len(fmt).replace(" ", "").count(":") - 1)], *[fmt.format(*r) if r else "" for r in rows]))

def show_status_table():
    tickets = load_tickets()
    if not tickets:
        print("Нет записей.")
        return
    headers = ["ID", "Тема", "Приоритет", "Статус", "Ответ"]
    rows = [[t["id"], t.get("subject",""), t.get("priority",""), t.get("status",""), t.get("reply","")] for t in tickets]
    print_table(headers, rows)

def show_all():
    statuses = ["new", "in_progress", "resolved", "escalated"]
    print(f"{'Приоритет':<15} {'Статус':<20} {'Количество':>10}")
    for p in ["low", "medium", "high", "urgent"]:
        count = sum(1 for t in load_tickets() if t.get("priority") == p)
        print(f"{p:<15} {', '.join(statuses):<20} {count:>10}")

if __name__ == "__main__":
    show_status_table()
