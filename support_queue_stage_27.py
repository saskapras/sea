# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: SupportQueue
def reset_demo_data():
    """Сбросить все демо-данные в дефолты."""
    global agents, tickets, messages, sla_config
    agents = {
        "support": {"name": "Support Bot", "role": "general"},
        "escalated": {"name": "Senior Support", "role": "escalation"},
    }
    tickets = {}
    messages = []
    sla_config = {
        "priority_levels": {
            "low": 720,
            "medium": 360,
            "high": 180,
            "critical": 60,
        },
        "status_transitions": {
            "open": ["responding", "escalated"],
            "responding": ["resolved", "escalated"],
            "escalated": ["resolved", "closed"],
            "resolved": ["closed"],
            "closed": [],
        },
        "priority_defaults": {"low": 1, "medium": 2, "high": 3, "critical": 4},
    }


def clear_state():
    """Полная очистка состояния приложения."""
    global agents, tickets, messages, sla_config
    agents = {}
    tickets = {}
    messages = []
    sla_config = {}
