# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: SupportQueue
def _is_duplicate(existing: list[dict], payload: dict) -> tuple[bool, int | None]:
    """Soft duplicate check: returns (is_dup, index) where index is the position of the first match, else None."""
    for i, record in enumerate(existing):
        if record.get("subject") == payload.get("subject"):
            return True, i
    return False, None
