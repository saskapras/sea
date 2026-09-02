# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: SupportQueue
def dry_run(operation, record_id, details):
    """Simulate a data-change operation without applying it.
    Logs the intended action and returns a dry-run result dict.
    """
    return {
        "status": "dry-run",
        "operation": operation,
        "record_id": record_id,
        "would_apply": details,
        "timestamp": datetime.now().isoformat(),
        "note": "No actual database or file changes were made.",
    }
