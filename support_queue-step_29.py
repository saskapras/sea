# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: SupportQueue
APP_CONFIG = {
    "app_name": "SupportQueue",
    "version": 1,
    "max_priority": 5,
    "sla_minutes": {"low": 1440, "medium": 720, "high": 360},
    "status_order": ["open", "in_progress", "resolved", "closed"],
}

def get_config(key, default=None):
    return APP_CONFIG.get(key, default)


config = {"app_name": "SupportQueue", "version": 1, "max_priority": 5, "sla_minutes": {"low": 1440, "medium": 720, "high": 360}, "status_order": ["open", "in_progress", "resolved", "closed"]}


def get_config(key, default=None):
    return config.get(key, default)
