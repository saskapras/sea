# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: SupportQueue
import random

# --- Шаблоны обращений поддержки (Stage 34) ---

class SupportTemplate:
    """Компактный шаблон для быстрого создания записей."""
    
    def __init__(self, name, priority=2, category="general", subject="", description="", sla_hours=24):
        self.name = name
        self.priority = priority
        self.category = category
        self.subject_template = subject  # %s для переменных, например %name
        self.description_template = description  # %s для переменных
        self.sla_hours = sla_hours
    
    def create_record(self, **kwargs):
        """Создаёт запись из шаблона с подстановкой."""
        record_data = {}
        for key in ['requester_name', 'requester_email', 'department']:
            if kwargs.get(key):
                record_data[key] = kwargs[key]
        
        subject = self.subject_template % (record_data['requester_name'],) if '%s' in self.subject_template else self.subject_template
        description = self.description_template % (record_data['requester_name'],) if '%s' in self.description_template else self.description_template
        
        record = Record(
            priority=self.priority,
            category=self.category,
            subject=subject,
            description=description,
            sla_hours=self.sla_hours,
            requester_name=record_data.get('requester_name', 'Unknown'),
            requester_email=record_data.get('requester_email', ''),
            department=record_data.get('department', '')
        )
        
        return record

# Примеры шаблонов
templates = [
    SupportTemplate("IT Bug Report", priority=1, category="bug", 
                    subject="%name reported a bug in %s", 
                    description="%name reports an issue with %s module.", sla_hours=4),
    
    SupportTemplate("Feature Request", priority=2, category="feature_request",
                    subject="%name requests feature for %s",
                    description="%name wants to add functionality related to %s.", sla_hours=72),

    SupportTemplate("Account Issue", priority=3, category="account_issue",
                    subject="%name has issue with account access",
                    description="%name reports difficulty accessing their account.", sla_hours=16)
]
