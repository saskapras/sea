# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: SupportQueue
def generate_monthly_stats(records):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'resolved': 0, 'avg_resolution_hours': []})
    for r in records:
        date_key = r['created_at'].strftime('%Y-%m') if isinstance(r['created_at'], str) else f"{r['created_at'][:4]}-{r['created_at'][5:7]}"
        stats[date_key]['total'] += 1
        if r.get('status') == 'resolved':
            stats[date_key]['resolved'] += 1
            res_hours = (r['updated_at'].timestamp() - r['created_at'].timestamp()) / 3600.0 if isinstance(r['updated_at'], str) else None
            if res_hours is not None:
                stats[date_key]['avg_resolution_hours'].append(res_hours)
    result = {}
    for month, data in sorted(stats.items()):
        avg_res = sum(data['avg_resolution_hours']) / len(data['avg_resolution_hours']) if data['avg_resolution_hours'] else 0.0
        result[month] = {
            'total_tickets': data['total'],
            'resolved_tickets': data['resolved'],
            'resolution_rate': (data['resolved'] / data['total'] * 100) if data['total'] > 0 else 0,
            'avg_resolution_hours': round(avg_res, 2)
        }
    return result
