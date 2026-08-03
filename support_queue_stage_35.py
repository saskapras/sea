# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: SupportQueue
def next_action(rec):
    """Return a short recommendation based on the current ticket state."""
    status = rec.get("status", "").lower()
    priority = rec.get("priority", "medium").lower()
    sla_hours = rec.get("sla_hours", 48)
    elapsed = (rec.get("created_at") or "")[:16]

    if status == "open":
        if priority in ("high", "critical"):
            return f"High priority open ticket – assign to senior agent ASAP."
        elif not rec.get("assigned_to"):
            return "Open ticket without assignee – pick a free agent from the pool."
        else:
            return "Open ticket with assignee – wait for first response or escalate if silent."

    if status == "pending":
        return "Ticket is pending information – send a polite follow-up reminder to the customer."

    if status == "escalated":
        return "Escalation active – involve team lead and check SLA compliance immediately."

    if status in ("resolved", "closed"):
        return None  # no further action needed

    if rec.get("sla_breached") or (elapsed and int(elapsed) > sla_hours):
        return f"SLA breached for {rec['id']}: notify customer of delay and propose workaround."

    return "No urgent action required – continue normal processing."
