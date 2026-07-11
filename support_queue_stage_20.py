# === Stage 20: Добавь восстановление записей из архива ===
# Project: SupportQueue
def restore_from_archive(archive_path, records):
    """Restore archived support tickets back into the active queue."""
    with open(archive_path, 'r') as f:
        lines = f.readlines()
    
    restored_count = 0
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 7:
            ticket_id, priority, subject, description, status, assigned_to, created_at = [p.strip() for p in parts]
            
            if status == "archived":
                records.append({
                    'ticket_id': ticket_id,
                    'priority': int(priority),
                    'subject': subject,
                    'description': description,
                    'status': 'new',  # Reset to active status
                    'assigned_to': assigned_to if assigned_to != 'none' else None,
                    'created_at': created_at,
                })
                restored_count += 1
    
    print(f"Restored {restored_count} tickets from archive")
