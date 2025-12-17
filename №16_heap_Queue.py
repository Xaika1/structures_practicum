import heapq


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._counter = 0

    def push(self, value, priority):
        heapq.heappush(self._heap, (priority, self._counter, value))
        self._counter += 1

    def pop(self):
        if not self._heap:
            return None
        priority, _, value = heapq.heappop(self._heap)
        return value, priority

    def is_empty(self):
        return not self._heap


class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


def schedule_tasks(tasks):
    pq = PriorityQueue()
    for t in tasks:
        pq.push(t, t.priority)

    order = []
    while not pq.is_empty():
        task, pr = pq.pop()
        order.append((task.name, pr))
    return order


def k_smallest(arr, k):
    if k <= 0:
        return []
    if k >= len(arr):
        return sorted(arr)
    heap = list(arr)
    heapq.heapify(heap)
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap))
    return result


def test_priority_queue():
    pq = PriorityQueue()
    pq.push("low", 5)
    pq.push("high", 1)
    pq.push("medium", 3)

    v1, p1 = pq.pop()
    v2, p2 = pq.pop()
    v3, p3 = pq.pop()
    assert (v1, p1) == ("high", 1)
    assert (v2, p2) == ("medium", 3)
    assert (v3, p3) == ("low", 5)
    assert pq.pop() is None

    tasks = [
        Task("Write report", 2),
        Task("Fix critical bug", 0),
        Task("Answer email", 5),
        Task("Code review", 1),
    ]
    scheduled = schedule_tasks(tasks)
    assert [name for name, _ in scheduled] == [
        "Fix critical bug",
        "Code review",
        "Write report",
        "Answer email",
    ]

    arr = [7, 2, 5, 1, 9, 3]
    assert k_smallest(arr, 0) == []
    assert k_smallest(arr, 1) == [1]
    assert k_smallest(arr, 3) == [1, 2, 3]
    assert k_smallest(arr, 6) == sorted(arr)

    print("Все тесты приоритетной очереди пройдены успешно!")


if __name__ == "__main__":
    test_priority_queue()
