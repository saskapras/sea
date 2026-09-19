# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: SupportQueue
def export_report(queue):
    """Export a brief text report of the support queue."""
    lines = ["=== Support Queue Report ===", f"Total tickets: {len(queue)}", ""]
    if not queue:
        lines.append("No tickets found.")
        return "\n".join(lines)
    status_counts = {}
    for t in queue:
        status_counts[t['status']] = status_counts.get(t['status'], 0) + 1
    lines.append("Status summary:")
    for s, c in sorted(status_counts.items()):
        lines.append(f"  {s}: {c}")
    lines.append("")
    for t in sorted(queue, key=lambda x: x['priority']):
        lines.append(f"[{t['priority']}] {t['id']} - {t['subject']} [{t['status']}]")
        if 'notes' in t:
            lines.append(f"  Notes: {t['notes']}")
        if 'sla' in t:
            lines.append(f"  SLA: {t['sla']}")
    return "\n".join(lines)
