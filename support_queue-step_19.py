# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: SupportQueue
def archive_support_tickets(self, max_age_days=30):
    """Archive completed or stale support tickets older than max_age_days."""
    cutoff = time.time() - (max_age_days * 86400)
    archived = []
    for ticket in self._tickets:
        if not self.is_active(ticket.id):
            age = (time.time() - ticket.created_at) / 86400
            if age >= max_age_days or ticket.status == "resolved":
                ticket.archived = True
                archived.append(ticket)
    return archived
