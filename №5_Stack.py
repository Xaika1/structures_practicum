
# Стек на массиве

class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# Стек на связном списке
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top_node = None

    def push(self, value):
        node = Node(value)
        node.next = self.top_node
        self.top_node = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        value = self.top_node.value
        self.top_node = self.top_node.next
        return value

    def top(self):
        if self.is_empty():
            return None
        return self.top_node.value

    def is_empty(self):
        return self.top_node is None



# Проверка корректности скобочной последовательности

def check_brackets(expression):
    stack = ArrayStack()  #можно заменить на LinkedListStack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expression:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    tests = ["()", "([]{})", "([)]", "((()))", "(", "())("]
    for t in tests:
        print(f"{t} → {check_brackets(t)}")

    print("\nТест стека на массиве:")
    s1 = ArrayStack()
    s1.push(10)
    s1.push(20)
    print("Верхний элемент:", s1.top())
    print("Извлечён:", s1.pop())
    print("Верхний элемент:", s1.top())

    print("\nТест стека на связном списке:")
    s2 = LinkedListStack()
    s2.push(100)
    s2.push(200)
    print("Верхний элемент:", s2.top())
    print("Извлечён:", s2.pop())
    print("Верхний элемент:", s2.top())