# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: SupportQueue
def undo_last_action(operations: list) -> None:
    """Откат последнего действия, если оно было записано в operations."""
    if not operations:
        return
    op = operations[-1]
    actions_map = {
        "create": ("remove",),
        "update_status": ("revert_status",),
        "set_priority": ("revert_priority",),
        "add_reply": ("delete_reply",),
        "escalate": ("unescalate",),
    }
    if op["action"] in actions_map:
        action = actions_map[op["action"]]
        if action[0] == "remove":
            ticket_id = op.get("ticket_id")
            reply_id = op.get("reply_id")
            for t in tickets:
                if t.id == ticket_id and any(r.id == reply_id for r in t.replies):
                    t.replies.remove(t.replies[-1])
        elif action[0] == "revert_status":
            old_status = op.get("old_status")
            for t in tickets:
                if t.id == op.get("ticket_id") and t.status == old_status:
                    # статус уже восстановлен, ничего не делаем
                    return
