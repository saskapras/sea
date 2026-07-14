# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: SupportQueue
def add_reminders():
    reminders = []

    def add_reminder(task_id, due_date):
        reminders.append({"task_id": task_id, "due_date": due_date})

    def check_and_log_expiry(reminders, today):
        expired = [r for r in reminders if r["due_date"] < today]
        for r in expired:
            print(f"Reminder expired: Task {r['task_id']} was due on {r['due_date']}")
        return expired

    def get_upcoming(reminders, days=7):
        upcoming = [r for r in reminders if 0 <= (today - r["due_date"]) <= days]
        return upcoming

    add_reminder(101, "2024-06-05")
    add_reminder(102, "2024-07-20")
    print(f"Total reminders: {len(reminders)}")
    print(check_and_log_expiry(reminders, today) or "No expired reminders")
    print(get_upcoming(reminders))

add_reminders()
