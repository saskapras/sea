# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: SupportQueue
def add_tags(self, tags):
    for tag in tags:
        if tag not in self.tags:
            self.tags.add(tag)
            return True
    return False

def remove_tags(self, tags):
    removed = []
    for tag in tags:
        if tag in self.tags:
            self.tags.discard(tag)
            removed.append(tag)
    return removed
