# === Stage 43: Добавь пагинацию длинных списков ===
# Project: SupportQueue
def paginate(items, page_size=10, page=1):
    if page < 1:
        page = 1
    if page_size < 1:
        page_size = 10
    total_pages = (len(items) + page_size - 1) // page_size
    total_pages = max(1, total_pages)
    start = (page - 1) * page_size
    end = start + page_size
    return {
        "items": items[start:end],
        "page": page,
        "page_size": page_size,
        "total": len(items),
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1,
    }
