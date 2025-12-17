class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DLLIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return node

    def insert_after(self, node, value):
   
        new_node = Node(value)


        if node is None:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
            return new_node

        nxt = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = nxt

        if nxt:
            nxt.prev = new_node
        else:
            self.tail = new_node

        return new_node

    def delete_node(self, node):

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def __iter__(self):
        return DLLIterator(self.head)


if __name__ == "__main__":
    lst = DoublyLinkedList()

    lst.head = Node(1)
    lst.tail = lst.head

    n2 = lst.insert_after(lst.head, 2)

    n3 = lst.insert_after(n2, 3)

    print("Список после вставок:")
    for x in lst:
        print(x)

    lst.delete(n2)

    print("Список после удаления 2:")
    for x in lst:
        print(x)