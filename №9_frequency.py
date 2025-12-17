import time
import re
from collections import defaultdict


class BadHash:
    
    def __call__(self, key):
        return 1


class GoodHash:
    
    def __call__(self, key):
        return hash(key)


class FrequencyDictionary:

    
    def __init__(self, hash_function=None):
        self.hash_function = hash_function if hash_function else hash
    
    def clean_text(self, text):
     
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    def build_frequency_dict(self, text):
        words = self.clean_text(text).split()
        freq_dict = {}
        
        for word in words:
            if word:
                if word in freq_dict:
                    freq_dict[word] += 1
                else:
                    freq_dict[word] = 1
        
        return freq_dict
    
    def get_top_words(self, freq_dict, n=10):
        """Получение N самых частых слов"""
        return sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:n]
    
    def benchmark_hash_functions(self, text):
        """Сравнение производительности разных хэш-функций"""
        
        print("\nСравнение производительности хэш-функций:")
        print("-" * 45)
        
        self.hash_function = GoodHash()
        start_time = time.time()
        freq_good = self.build_frequency_dict(text)
        good_time = time.time() - start_time
        
        print(f"Хорошая хэш-функция: {good_time:.6f} секунд")
        
        self.hash_function = BadHash()
        start_time = time.time()
        freq_bad = self.build_frequency_dict(text)
        bad_time = time.time() - start_time
        
        print(f"Плохая хэш-функция:  {bad_time:.6f} секунд")
        
        if good_time > 0:
            slowdown = bad_time / good_time
            print(f"\nПлохая функция медленнее в {slowdown:.1f} раз")
        
        self.hash_function = hash
        
        return freq_good, freq_bad, good_time, bad_time


def test_frequency_dictionary():

    print("ТЕСТИРОВАНИЕ ЧАСТОТНОГО СЛОВАРЯ")
    
    sample_text = """
    Программирование — это искусство и наука создания программ.
    Хороший программист должен обладать логическим мышлением, 
    вниманием к деталям и способностью решать сложные задачи.
    Python является отличным языком программирования для начинающих
    и профессионалов. Программирование на Python приносит удовольствие
    и позволяет быстро создавать эффективные приложения.
    Искусство программирования заключается в умении разбивать
    большие задачи на маленькие и решать их по отдельности.
    Программирование требует постоянного обучения и практики.
    """
    
    print("Текст для анализа:")
    print(sample_text[:200] + "...")
    
    analyzer = FrequencyDictionary()
    
    print("\n1. Построение частотного словаря:")
    
    freq_dict = analyzer.build_frequency_dict(sample_text)
    total_words = sum(freq_dict.values())
    unique_words = len(freq_dict)
    
    print(f"Всего слов в тексте: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    
    print("\n2. Топ-10 самых частых слов:")
    
    top_words = analyzer.get_top_words(freq_dict, 10)
    for i, (word, count) in enumerate(top_words, 1):
        percentage = (count / total_words) * 100
        print(f"{i:2}. {word:15} — {count:3} раз ({percentage:.1f}%)")
    
    print("\n3. Распределение частот слов:")
    
    freq_distribution = defaultdict(int)
    for count in freq_dict.values():
        if count == 1:
            freq_distribution["1 раз"] += 1
        elif count <= 5:
            freq_distribution["2-5 раз"] += 1
        elif count <= 10:
            freq_distribution["6-10 раз"] += 1
        else:
            freq_distribution[">10 раз"] += 1
    
    for category, count in sorted(freq_distribution.items()):
        percentage = (count / unique_words) * 100
        print(f"{category:10} — {count:3} слов ({percentage:.1f}%)")
    
    print("\n4. Тестирование на разных объемах текста:")

    base_word = "слово"
    small_text = " ".join([base_word] * 100)
    medium_text = " ".join([base_word] * 1000)
    large_text = " ".join([base_word] * 10000)
    
    test_cases = [
        ("Маленький (100 слов)", small_text),
        ("Средний (1000 слов)", medium_text),
        ("Большой (10000 слов)", large_text)
    ]
    
    results = []
    
    for name, text in test_cases:
        print(f"\n{name}:")
        freq_good, freq_bad, good_time, bad_time = analyzer.benchmark_hash_functions(text)
        
        if good_time > 0:
            slowdown = bad_time / good_time
            results.append((name, good_time, bad_time, slowdown))
    
    print("\n5. Итоги сравнения:")
    print(f"{'Размер текста':<20} {'Хорошая':<10} {'Плохая':<10} {'Замедление':<10}")
    
    for name, good_time, bad_time, slowdown in results:
        print(f"{name:<20} {good_time:.6f}  {bad_time:.6f}  {slowdown:>8.1f}x")
    
    print("ВЫВОДЫ:")
    print("""
    1. Хорошая хэш-функция обеспечивает равномерное распределение
       ключей, что приводит к O(1) времени доступа в среднем.
       
    2. Плохая хэш-функция (возвращающая одно значение) вырождает
       хэш-таблицу в связный список с временем доступа O(n).
       
    3. На больших объемах данных разница в производительности
       становится особенно заметной (в десятки раз).
       
    4. Качество хэш-функции критически важно для эффективности
       работы хэш-таблицы.
    """)


if __name__ == "__main__":
    test_frequency_dictionary()