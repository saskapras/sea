# === Stage 59: Добавь диагностику производительности основных операций ===
# Project: SupportQueue
def profile_support_queue():
    """Диагностика производительности основных операций с обращением к реальному объекту."""
    from timeit import default_timer as timer

    if not globals().get("queue"):
        print("[profile] Не найден объект queue — создаю тестовый.")
        queue = SupportQueue()
        for i in range(200):
            queue.create_ticket(
                subject=f"Тикет #{i}",
                priority=random.randint(1, 4),
                description="Тестовое обращение для диагностики.",
            )

    n = len(queue)
    print(f"[profile] Обработано обращений в трекере: {n}")

    def timeit(label, func, *args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        elapsed = timer() - start
        print(f"[profile] {label:<24} {elapsed * 1e3:8.3f} мс")

    timeit("create_ticket", queue.create_ticket,
           subject="Профиль", priority=2, description="Тест.")
    timeit("get_ticket", queue.get_ticket, 1)
    timeit("update_status", queue.update_status, 1, "open")
    timeit("add_reply", queue.add_reply, 1, "Это ответ.", author="Агент")
    timeit("list_tickets", queue.list_tickets)

    if hasattr(queue, "get_sla_status"):
        timeit("get_sla_status", queue.get_sla_status, 1)

    print("[profile] Диагностика завершена.")
