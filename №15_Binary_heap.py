class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapify_down(self, i):
        n = len(self.heap)
        while True:
            min_idx = i
            left_idx = self.left(i)
            right_idx = self.right(i)

            if left_idx < n and self.heap[left_idx] < self.heap[min_idx]:
                min_idx = left_idx
            if right_idx < n and self.heap[right_idx] < self.heap[min_idx]:
                min_idx = right_idx

            if min_idx == i:
                break

            self.swap(i, min_idx)
            i = min_idx

    def extract_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.heapify_down(0)
        return min_val
    
    def is_valid_heap(self):
        n = len(self.heap)
        for i in range(n):
            left = self.left(i)
            right = self.right(i)
            if left < n and self.heap[i] > self.heap[left]:
                return False
            if right < n and self.heap[i] > self.heap[right]:
                return False
        return True

    @staticmethod
    def build_heap(arr):
        heap = MinHeap()
        heap.heap = arr[:]
        for i in range(len(arr) // 2 - 1, -1, -1):
            heap.heapify_down(i)
        return heap


if __name__ == "__main__":
    initial = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = MinHeap.build_heap(initial)
    print("Построенная куча:", heap.heap)
    print("Корень (минимум):", heap.heap[0])
    print("Куча валидна после build_heap:", heap.is_valid_heap())

    heap.insert(5)
    print("После вставки 5:", heap.heap)
    print("Куча валидна после insert:", heap.is_valid_heap())

    min_val = heap.extract_min()
    print("Извлечён минимум:", min_val)
    print("После extract_min:", heap.heap)
    print("Куча валидна после extract_min:", heap.is_valid_heap())
