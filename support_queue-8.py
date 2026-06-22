# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: SupportQueue
def show_menu():
    print("\n=== Меню SupportQueue ===")
    print("1. Показать все заявки")
    print("2. Добавить новую заявку")
    print("3. Изменить статус/приоритет")
    print("4. Проверить SLA (просроченные)")
    print("5. Вывести статистику")
    print("0. Выход")

def run_command(cmd):
    if cmd == "1":
        for t in tickets:
            print(f"[{t['id']}] {t['subject']} | Статус: {t['status']} | Приоритет: {t['priority']}")
    elif cmd == "2":
        subj = input("Тема заявки: ")
        desc = input("Описание: ")
        pri = int(input("Приоритет (1-3): ")) or 2
        tickets.append({"id": len(tickets)+1, "subject": subj, "desc": desc, "status": "new", "priority": pri})
    elif cmd == "3":
        idx = int(input("ID заявки: ")) - 1
        if 0 <= idx < len(tickets):
            t = tickets[idx]
            print(f"Текущий статус: {t['status']}, приоритет: {t['priority']}")
            new_status = input("Новый статус (new/open/in_progress/resolved/closed): ") or t["status"]
            new_priority = int(input("Новый приоритет (1-3): ")) or t["priority"]
            tickets[idx]["status"] = new_status
            tickets[idx]["priority"] = new_priority
    elif cmd == "4":
        now = datetime.now()
        for t in tickets:
            if t["status"] != "closed" and (t.get("created_at") is None or (now - t["created_at"]).total_seconds() > 3600 * 24):
                print(f"[{t['id']}] {t['subject']} — SLA нарушен!")
    elif cmd == "5":
        stats = {"new": 0, "open": 0, "in_progress": 0, "resolved": 0, "closed": 0}
        for t in tickets:
            s = t["status"]
            if s in stats: stats[s] += 1
        print("Статистика:", stats)

def main():
    global tickets
    while True:
        show_menu()
        cmd = input("Введите команду: ")
        run_command(cmd)
        if cmd == "0": break

# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: SupportQueue
def print_menu():
    print("\n=== Меню поддержки ===")
    print("1. Показать все заявки")
    print("2. Добавить новую заявку")
    print("3. Изменить статус/приоритет")
    print("4. Проверить SLA (просроченные)")
    print("5. Вывести статистику")
    print("6. Сохранить и выйти")

def handle_command(cmd):
    if cmd == '1':
        for t in tickets:
            print(f"[{t['id']}] {t['subject']} | Статус: {t['status']} | Приоритет: {t['priority']}")
    elif cmd == '2':
        subj = input("Тема: ")
        desc = input("Описание: ")
        pri = int(input("Приоритет (1-3): ")) or 2
        new_ticket = {'id': len(tickets)+1, 'subject': subj, 'desc': desc, 'status': 'new', 'priority': pri}
        tickets.append(new_ticket)
        print(f"Заявка {new_ticket['id']} создана.")
    elif cmd == '3':
        tid = int(input("ID заявки: ")) - 1
        if tid < len(tickets):
            st = input("Новый статус (new, in_progress, resolved): ") or tickets[tid]['status']
            pr = int(input("Новый приоритет (1-3): ")) or tickets[tid]['priority']
            tickets[tid]['status'] = st
            tickets[tid]['priority'] = pr
            print(f"Заявка {tid+1} обновлена.")
    elif cmd == '4':
        now = datetime.now()
        for t in tickets:
            if t['status'] != 'resolved' and (t.get('created_at') or now).replace(tzinfo=None) < now - timedelta(hours=2):
                print(f"⚠️ SLA нарушен для заявки {t['id']}: {t['subject']}")
    elif cmd == '5':
        stats = {'new': 0, 'in_progress': 0, 'resolved': 0}
        for t in tickets: stats[t['status']] += 1
        print(f"Статистика: новых={stats['new']}, в работе={stats['in_progress']}, решено={stats['resolved']}")
    elif cmd == '6':
        save_file()
        exit(0)

while True:
    print_menu()
    choice = input("Ваш выбор (1-6): ")
    if not choice.isdigit(): continue
    handle_command(choice)
