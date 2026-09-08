# === Stage 45: Добавь восстановление из резервной копии ===
# Project: SupportQueue
def restore_from_backup(backup_path, file_path):
    try:
        with open(backup_path, 'r') as f:
            lines = f.readlines()
        with open(file_path, 'w') as f:
            for line in lines:
                f.write(line)
        print(f"Backup restored from {backup_path} to {file_path}")
    except FileNotFoundError:
        print(f"Backup file not found: {backup_path}")
    except Exception as e:
        print(f"Restore failed: {e}")
