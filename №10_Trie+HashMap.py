import re


class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0
        self.word = None


class TrieAutocomplete:
    
    def __init__(self):
        self.root = TrieNode()
        self.word_frequencies = {}
    
    def insert(self, word, frequency=1):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        node.frequency += frequency
        node.word = word
        
        self.word_frequencies[word] = node.frequency
    
    def search(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def search_with_frequency(self, word):

        node = self.root
        
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        
        return node.frequency if node.is_end_of_word else None
    
    def _collect_words(self, node, results):
        if node.is_end_of_word:
            results.append((node.word, node.frequency))
        
        for child_node in node.children.values():
            self._collect_words(child_node, results)
    
    def autocomplete(self, prefix, limit=5):
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        self._collect_words(node, results)
        
        results.sort(key=lambda x: x[1], reverse=True)
        
        return [word for word, _ in results[:limit]]
    
    def autocomplete_with_frequencies(self, prefix, limit=5):
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []
        self._collect_words(node, results)
        
        results.sort(key=lambda x: x[1], reverse=True)
        
        return results[:limit]
    
    def add_from_text(self, text):
        words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b', text.lower())
        
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        
        for word, count in word_counts.items():
            self.insert(word, count)
        
        return word_counts
    
    def get_suggestions(self, prefix, limit=5):
        suggestions = self.autocomplete_with_frequencies(prefix, limit)
        
        if not suggestions:
            return []
        
        result = []
        total_freq = sum(freq for _, freq in suggestions)
        
        for word, freq in suggestions:
            percentage = (freq / total_freq) * 100 if total_freq > 0 else 0
            result.append({
                'word': word,
                'frequency': freq,
                'percentage': percentage
            })
        
        return result
    
    def print_trie(self, node=None, prefix="", level=0):
        if node is None:
            node = self.root
        
        indent = "  " * level
        node_info = ""
        
        if node.is_end_of_word:
            node_info = f" [СЛОВО: '{node.word}', ЧАСТОТА: {node.frequency}]"
        
        print(f"{indent}{prefix}{node_info}")
        
        for char, child_node in sorted(node.children.items()):
            self.print_trie(child_node, char, level + 1)


def test_autocomplete_system():
    
    print("ТЕСТИРОВАНИЕ СИСТЕМЫ АВТОДОПОЛНЕНИЯ")
    
    trie = TrieAutocomplete()
    
    print("1. Инициализация системы словами с частотами:")
    
    initial_words = [
        ("программирование", 150),
        ("программа", 120),
        ("процесс", 80),
        ("процессор", 60),
        ("профессия", 40),
        ("проект", 90),
        ("прогресс", 70),
        ("тестирование", 110),
        ("тест", 200),
        ("текст", 95),
        ("технология", 85),
        ("алгоритм", 130),
        ("анализ", 75),
        ("база", 50),
        ("база данных", 65),
        ("баланс", 30),
        ("простой", 55),
        ("процедура", 45),
        ("производительность", 35)
    ]
    
    for word, freq in initial_words:
        trie.insert(word, freq)
        print(f"Добавлено: '{word}' (частота: {freq})")
    
    print(f"\nВсего слов в системе: {len(trie.word_frequencies)}")
    
    print("\n2. Тестирование автодополнения:")

    
    test_prefixes = [
        ("про", 5),
        ("те", 3),
        ("алг", 5),
        ("ба", 4),
        ("прог", 5),
        ("проц", 3),
        ("ан", 3),
        ("тех", 3)
    ]
    
    for prefix, limit in test_prefixes:
        suggestions = trie.get_suggestions(prefix, limit)
        
        print(f"\nПрефикс: '{prefix}' (макс. {limit} предложений):")
        
        if suggestions:
            for i, suggestion in enumerate(suggestions, 1):
                word = suggestion['word']
                freq = suggestion['frequency']
                perc = suggestion['percentage']
                print(f"  {i}. {word:25} [частота: {freq:3}, {perc:5.1f}%]")
        else:
            print("  Нет предложений")
    
    print("\n3. Тестирование поиска слов:")
    
    test_words = [
        "программа",
        "тест", 
        "алгоритм",
        "несуществующее",
        "база данных",
        "процесс"
    ]
    
    for word in test_words:
        freq = trie.search_with_frequency(word)
        if freq is not None:
            print(f"Слово '{word}' найдено (частота: {freq})")
        else:
            print(f"Слово '{word}' не найдено")
    
    print("\n4. Добавление текста и обновление частот:")
    
    new_text = """
    Программирование на Python это интересно и увлекательно.
    Тестирование программ является важной частью разработки.
    Алгоритмы должны быть эффективными и понятными.
    Программирование требует постоянной практики и изучения нового.
    Тестирование помогает находить ошибки в коде.
    База данных хранит информацию о пользователях и их действиях.
    Процесс разработки включает проектирование, кодирование и тестирование.
    """
    
    print("Новый текст для анализа:")
    print(new_text[:150] + "...")
    
    new_words = trie.add_from_text(new_text)
    
    print(f"\nДобавлено/обновлено {len(new_words)} слов из текста")
    
    print("\nОбновленные топ-5 слов:")
    sorted_words = sorted(trie.word_frequencies.items(), 
                         key=lambda x: x[1], reverse=True)[:5]
    for word, freq in sorted_words:
        print(f"  {word:25} — {freq:3}")
    
    print("\n5. Проверка автодополнения после обновления:")
    suggestions = trie.get_suggestions("про", 5)
    print("Автодополнение для 'про' (после обновления):")
    for i, suggestion in enumerate(suggestions, 1):
        word = suggestion['word']
        freq = suggestion['frequency']
        print(f"  {i}. {word:25} [частота: {freq}]")
    
    print("\n6. Структура Trie (первые 3 уровня):")
    print("(Для наглядности показываем только начало структуры)")
    
    def print_partial_trie(node, prefix="", level=0, max_level=3):
        if level > max_level:
            return
        
        indent = "  " * level
        node_info = ""
        
        if node.is_end_of_word and level > 0:
            node_info = f" ← '{node.word}'"
        
        if level == 0:
            print(f"{indent}корень")
        else:
            print(f"{indent}{prefix}{node_info}")
        
        for char, child_node in sorted(node.children.items()):
            print_partial_trie(child_node, char, level + 1, max_level)
    
    print_partial_trie(trie.root, max_level=3)
    
    print("ИТОГИ ТЕСТИРОВАНИЯ:")
    print("""
    1. Система автодополнения успешно построена на основе:
       - Trie (префиксного дерева) для быстрого поиска по префиксу
       - HashMap для хранения частот слов и быстрого доступа
    
    2. Преимущества подхода:
       - Быстрый поиск по префиксу: O(k), где k - длина префикса
       - Сортировка по частоте использования
       - Эффективное обновление частот
       - Поддержка слов с пробелами и разной длины
    
    3. Применение:
       - Поисковые системы
       - Текстовые редакторы
       - Мобильные клавиатуры
       - Системы рекомендаций
    """)


if __name__ == "__main__":
    test_autocomplete_system()