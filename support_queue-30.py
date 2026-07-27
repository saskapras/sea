# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: SupportQueue
class Profile:
    def __init__(self, name, role='user', priority=0):
        self.name = name
        self.role = role
        self.priority = priority

    def __repr__(self):
        return f"Profile(name={self.name}, role={self.role})"


class ProfileManager:
    _profiles = {
        'admin': Profile('admin', 'admin', 3),
        'support': Profile('support_agent', 'support', 1),
        'user': Profile('customer', 'user', 0),
    }

    @classmethod
    def get_profile(cls, name):
        return cls._profiles.get(name)

    @classmethod
    def register(cls, name, role='user'):
        if name in cls._profiles:
            raise ValueError(f"Profile '{name}' already exists")
        cls._profiles[name] = Profile(name, role)
        return cls._profiles[name]

    @classmethod
    def all_profiles(cls):
        return list(cls._profiles.values())
