# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: SupportQueue
def export_state_to_json():
    import json
    state = {
        "tickets": tickets,
        "agents": agents,
        "config": config
    }
    return json.dumps(state, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print(export_state_to_json())
