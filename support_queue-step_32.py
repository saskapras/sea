# === Stage 32: Добавь журнал действий пользователя ===
# Project: SupportQueue
def log_action(user, action_type, details):
    """Add an entry to the user's activity journal."""
    if not hasattr(user, 'journal'):
        user.journal = []
    entry = {
        'timestamp': datetime.now().isoformat(),
        'user_id': user.id,
        'action': action_type,
        'details': details
    }
    user.journal.append(entry)
