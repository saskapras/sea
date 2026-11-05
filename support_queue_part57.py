# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: SupportQueue
def batch_delete(queue, ids, confirm=False):
    if confirm:
        print("Удалить следующие обращения? (введите 'yes' для подтверждения):")
        for t in queue:
            print("  #" + str(t["id"]) + " [" + t["priority"] + "] " + t["subject"] + " - " + t["status"])
        response = input("> ")
        if response.lower() != "yes":
            print("Отмена.")
            return False
    to_delete = [t for t in queue if t["id"] in ids]
    if not to_delete:
        print("Обращений с указанными ID не найдено.")
        return False
    for t in to_delete:
        queue.remove(t)
    print("Удалено обращений: " + str(len(to_delete)))
    return True
