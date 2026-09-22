# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: SupportQueue
class FavoritesManager:
    def __init__(self):
        self._favorites = set()

    def add(self, item_id):
        self._favorites.add(item_id)

    def remove(self, item_id):
        self._favorites.discard(item_id)

    def is_favorited(self, item_id):
        return item_id in self._favorites

    def toggle(self, item_id):
        if self.is_favorited(item_id):
            self.remove(item_id)
        else:
            self.add(item_id)

    def get_favorites(self):
        return list(self._favorites)

    def clear(self):
        self._favorites.clear()

    def __len__(self):
        return len(self._favorites)
