class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None     

class LinkedList:
    def __init__(self):
        self.head = None    

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head 
        self.head = new_node       

    def push_back(self, value):
        new_node = Node(value)
        if self.head is None:     
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None: 
            cur = cur.next
        cur.next = new_node        

   
    def remove(self, value):
        cur = self.head
        prev = None
        while cur is not None:
            if cur.value == value:
                if prev is None:        
                    self.head = cur.next
                else:                  
                    prev.next = cur.next
                return
            prev = cur
            cur = cur.next


    def find(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next
        return False


    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            nxt = cur.next  
            cur.next = prev 
            cur = nxt
        self.head = prev 
if __name__ == '__main__':
    lst = LinkedList()
    lst.push_front(2)
    lst.push_front(1)
    lst.push_back(3)
    lst.push_back(4)
    lst.print_list()      

    lst.remove(3)
    lst.print_list()      

    print(lst.find(2))    
    print(lst.find(10))    

    lst.reverse()
    lst.print_list() 
    #В массиве вставка/удаление в начале и середине медленные, а в односвязном списке — быстрые, но поиск медленный.