# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: SupportQueue
def generate_weekly_stats(records):
    from collections import defaultdict
    stats = defaultdict(lambda: {'total': 0, 'resolved': 0, 'avg_response_time_sec': []})
    for r in records:
        date_key = (r['created_at'] + timedelta(days=1)).date() - timedelta(days=r['created_at'].weekday()) # Примерная логика группировки по неделям требует корректного определения начала недели.
        week_start = r['created_at'].replace(day=1) - timedelta(days=(r['created_at'].day - 1 + (7 - r['created_at'].weekday())) % 7)
        date_key = week_start.strftime('%Y-%W') # Недельный номер ISO
        stats[date_key]['total'] += 1
        if r['status'] == 'resolved':
            stats[date_key]['resolved'] += 1
        if r.get('response_time_sec', None):
            stats[date_key]['avg_response_time_sec'].append(r['response_time_sec'])
    result = []
    for week, data in sorted(stats.items()):
        avg_rt = sum(data['avg_response_time_sec']) / len(data['avg_response_time_sec']) if data['avg_response_time_sec'] else 0
        result.append({'week': week, 'total_tickets': data['total'], 'resolved_count': data['resolved'], 'sla_compliance_pct': (data['resolved']/data['total']*100) if data['total'] > 0 else 0, 'avg_response_time_sec': round(avg_rt, 2)})
    return result
