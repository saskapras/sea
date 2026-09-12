# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: SupportQueue
def _format_ticket(t: Ticket) -> str:
    return (
        f"[#{t.id}] {t.title} | "
        f"Priority: {t.priority} | "
        f"Status: {t.status} | "
        f"Created: {t.created} | "
        f"Agent: {t.agent} | "
        f"Customer: {t.customer} | "
        f"SLA met: {t.sla_met}"
    )
