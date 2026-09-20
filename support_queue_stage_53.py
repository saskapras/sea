# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: SupportQueue
def export_records(records, filename="support_queue.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for r in records:
            f.write(f"[{r['id']}] "
                     f"User: {r['user']} | "
                     f"Priority: {r['priority']} | "
                     f"Status: {r['status']} | "
                     f"Message: {r['message']}\n")
