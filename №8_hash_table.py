class HashNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class CustomHashTable:
    
    def __init__(self, capacity=16, load_factor=0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.buckets = [None] * capacity
    
    def hash_function(self, key):
        if isinstance(key, str):
            hash_val = 5381
            for char in key:
                hash_val = ((hash_val << 5) + hash_val) + ord(char)
            return hash_val % self.capacity
        else:
            return hash(key) % self.capacity
    
    def put(self, key, value):
        if self.size / self.capacity >= self.load_factor:
            self._rehash()
        
        index = self.hash_function(key)
        node = self.buckets[index]
        
        if node is None:
            self.buckets[index] = HashNode(key, value)
            self.size += 1
            return
        
        prev = None
        while node:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next
        
        prev.next = HashNode(key, value)
        self.size += 1
    
    def get(self, key):
        index = self.hash_function(key)
        node = self.buckets[index]
        
        while node:
            if node.key == key:
                return node.value
            node = node.next
        
        raise KeyError(f"Ключ '{key}' не найден")
    
    def remove(self, key):
        index = self.hash_function(key)
        node = self.buckets[index]
        prev = None
        
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] = node.next
                self.size -= 1
                return node.value
            prev = node
            node = node.next
        
        raise KeyError(f"Ключ '{key}' не найден")
    
    def contains(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def _rehash(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0
        
        for bucket in old_buckets:
            node = bucket
            while node:
                self.put(node.key, node.value)
                node = node.next
    
    def visualize(self):
        print(f"\nХэш-таблица (размер: {self.size}, емкость: {self.capacity})")
        
        for i, bucket in enumerate(self.buckets):
            chain = []
            node = bucket
            while node:
                chain.append(f"{node.key}:{node.value}")
                node = node.next
            
            if chain:
                print(f"[{i:3}] → {' → '.join(chain)}")
            else:
                print(f"[{i:3}] → пусто")
        
        load = self.size / self.capacity
        print(f"Коэффициент загрузки: {load:.2f} (порог: {self.load_factor})")


def test_hash_table():
    
    print("ТЕСТИРОВАНИЕ ХЭШ-ТАБЛИЦЫ")
    ht = CustomHashTable(capacity=5)
    print("Создана хэш-таблица с начальной емкостью 5")
    ht.visualize()
    
    print("\n1. Тест добавления элементов:")
    
    test_data = [
        ("яблоко", "фрукт", 1),
        ("банан", "фрукт", 2),
        ("вишня", "ягода", 3),
        ("дата", "фрукт", 4),
        ("бузина", "ягода", 5),
        ("инжир", "фрукт", 6),
        ("виноград", "ягода", 7),
        ("дыня", "бахча", 8)
    ]
    
    for key, value, step in test_data:
        ht.put(key, value)
        print(f"\nШаг {step}: Добавлено '{key}' -> '{value}'")
        ht.visualize()
    
    print("\n2. Тест получения элементов:")
    
    test_keys = ["банан", "виноград", "дыня"]
    for key in test_keys:
        try:
            value = ht.get(key)
            print(f"Ключ '{key}' -> значение '{value}'")
        except KeyError as e:
            print(f"Ошибка: {e}")
    
    print("\n3. Тест обновления элемента:")
    
    print("Обновляем значение 'банан' на 'тропический фрукт'")
    ht.put("банан", "тропический фрукт")
    print(f"Новое значение 'банана': {ht.get('банан')}")
    
    print("\n4. Тест удаления элементов:")

    keys_to_remove = ["вишня", "дата"]
    for key in keys_to_remove:
        try:
            removed_value = ht.remove(key)
            print(f"Удален ключ '{key}' со значением '{removed_value}'")
            ht.visualize()
        except KeyError as e:
            print(f"Ошибка при удалении: {e}")
    
    print("\n5. Тест проверки наличия ключей:")
    
    test_check_keys = ["яблоко", "вишня", "инжир", "несуществующий"]
    for key in test_check_keys:
        exists = ht.contains(key)
        print(f"Ключ '{key}': {'существует' if exists else 'не существует'}")
    
    print("\n6. Тест с числовыми ключами:")
    
    ht.put(123, "число")
    ht.put(456, "еще число")
    print(f"Ключ 123 -> {ht.get(123)}")
    print(f"Ключ 456 -> {ht.get(456)}")
    
    ht.visualize()
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")


if __name__ == "__main__":
    test_hash_table()