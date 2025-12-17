class CircularQueue:
    """Очередь на циклическом массиве"""
    
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self, item):
        if self.is_full():
            self._resize()
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.queue[self.front]
    
    def _resize(self):
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity
        
        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]
        
        self.queue = new_queue
        self.front = 0
        self.rear = self.size
        self.capacity = new_capacity
    
    def __str__(self):
        result = []
        for i in range(self.size):
            result.append(str(self.queue[(self.front + i) % self.capacity]))
        return f"[{', '.join(result)}]"


class QueueTwoStacks:
    """Очередь на двух стеках"""
    
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
    
    def enqueue(self, item):
        self.stack_in.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        
        return self.stack_out[-1]
    
    def is_empty(self):
        return not self.stack_in and not self.stack_out
    
    def __str__(self):
        return f"Входной стек: {self.stack_in}, Выходной стек: {self.stack_out}"


def test_queue_implementations():
    """Тестирование обеих реализаций очереди"""    
    #Тест циклической очереди
    print("\n1. Очередь на циклическом массиве:")
    
    cq = CircularQueue(5)
    print(f"Создана очередь с емкостью 5")
    print(f"Очередь пуста? {cq.is_empty()}")
    
    print("\nДобавляем элементы 1-7:")
    for i in range(1, 8):
        cq.enqueue(i)
        print(f"Добавили {i}: {cq}")
    
    print(f"\nПервый элемент (peek): {cq.peek()}")
    print(f"Извлекаем (dequeue): {cq.dequeue()}")
    print(f"Извлекаем (dequeue): {cq.dequeue()}")
    print(f"Текущая очередь: {cq}")
    print(f"Очередь пуста? {cq.is_empty()}")
    print(f"Текущая емкость: {cq.capacity}")
    
    # Тест очереди на двух стеках
    print("\n\n2. Очередь на двух стеках:")
    
    qts = QueueTwoStacks()
    print("Создана очередь на двух стеках")
    print(f"Очередь пуста? {qts.is_empty()}")
    
    print("\nДобавляем элементы A, B, C:")
    for char in ['A', 'B', 'C']:
        qts.enqueue(char)
        print(f"Добавили '{char}': {qts}")
    
    print(f"\nПервый элемент (peek): {qts.peek()}")
    print(f"Извлекаем (dequeue): {qts.dequeue()}")
    print(f"Текущее состояние: {qts}")
    
    print("\nДобавляем элементы D, E:")
    qts.enqueue('D')
    qts.enqueue('E')
    print(qts)
    
    print(f"\nИзвлекаем: {qts.dequeue()}")
    print(f"Извлекаем: {qts.dequeue()}")
    print(f"Очередь пуста? {qts.is_empty()}")
    print(f"Текущее состояние: {qts}")


if __name__ == "__main__":
    test_queue_implementations()