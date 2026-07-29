# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: SupportQueue
import json

def switch_profile(profile_name):
    profiles = {
        "admin": {"name": "Администратор", "role": "manager"},
        "user": {"name": "Пользователь", "role": "customer"},
        "agent": {"name": "Агент", "role": "support_agent"}
    }
    if profile_name not in profiles:
        print(f"Профиль '{profile_name}' не найден. Доступные: {list(profiles.keys())}")
        return None
    current = json.load(open("profiles.json"))
    updated = dict(current)
    updated["active_profile"] = profile_name
    with open("profiles.json", "w") as f:
        json.dump(updated, f, indent=2)
    print(f"Переключено на профиль: {profile_name} ({profiles[profile_name]['name']})")
    return profiles[profile_name]
