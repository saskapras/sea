# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: SupportQueue
import json, shutil, os
from datetime import datetime

def backup_data_file(data_path, backup_dir=None):
    if not os.path.exists(data_path):
        print(f"Файл данных не найден: {data_path}")
        return None
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(data_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(backup_dir, f"backup_{datetime.now():%Y%m%d_%H%M%S}.json")
    shutil.copy2(data_path, backup_path)
    print(f"Резервная копия сохранена: {backup_path}")
    return backup_path

def restore_data_file(data_path, backup_path):
    if not os.path.exists(backup_path):
        print(f"Файл резервной копии не найден: {backup_path}")
        return False
    shutil.copy2(backup_path, data_path)
    print(f"Данные восстановлены из: {backup_path}")
    return True
