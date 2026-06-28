# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: SupportQueue
def load_from_json(file_path):
    try:
        import json
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return [SupportTicket(**item) for item in data]
        elif isinstance(data, dict):
            return SupportTicket(**data)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON в файле {file_path}: {e}")
        return []
    except KeyError as e:
        print(f"Отсутствует обязательное поле {e} для записи.")
        return []
