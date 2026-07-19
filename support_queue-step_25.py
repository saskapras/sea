# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: SupportQueue
def validate_and_normalize_record(raw):
    try:
        user = raw.get('user') or raw.get('username', '')
        if not user.strip():
            raise ValueError("Пользователь обязателен и не может быть пустым.")

        priority = raw.get('priority', 'normal').lower()
        valid_prio = {'low': 3, 'normal': 2, 'high': 1}
        if priority not in valid_prio:
            raise ValueError(f"Неизвестный приоритет '{priority}'. Допустимы: low, normal, high.")

        status = raw.get('status', '').lower()
        valid_status = {'new', 'in_progress', 'resolved', 'closed'}
        if status not in valid_status:
            raise ValueError(f"Неизвестный статус '{status}'. Допустимые: new, in_progress, resolved, closed.")

        date_str = raw.get('date') or raw.get('created_at', '')
        if isinstance(date_str, str) and date_str.strip():
            try:
                parsed_date = datetime.strptime(date_str[:10], '%Y-%m-%d').date()
                today = datetime.now().date()
                if parsed_date > today + timedelta(days=2):
                    raise ValueError("Дата создания в будущем (более чем на 2 дня).")
            except Exception:
                raise ValueError(f"Некорректный формат даты '{date_str}'. Ожидается YYYY-MM-DD.")

        response = raw.get('response', '')
        if isinstance(response, str) and len(response.strip()) < 3:
            raise ValueError("Ответ слишком короткий. Минимум 3 символа.")

        return {
            'user': user.strip(),
            'priority': priority,
            'status': status,
            'date': parsed_date or datetime.now().date(),
            'response': response if isinstance(response, str) else '',
        }
    except Exception as e:
        raise RuntimeError(f"Ошибка валидации записи: {e}") from e
