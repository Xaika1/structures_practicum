import time

class Static:
    def __init__(self):
        self.arr = [0] * 100000 
        self.size = 0
    
    def add(self, x):
        if self.size < 100000:
            self.arr[self.size] = x
            self.size += 1

class Dynamic:
    def __init__(self):
        self.arr = [0] * 4    
        self.size = 0
        self.cap = 4
    
    def add(self, x):
        if self.size == self.cap:
            self.cap *= 2  
            self.arr += [0] * (self.cap - self.size)
        self.arr[self.size] = x
        self.size += 1

print("Тест 100000 элементов...")

t1 = time.time()
s = Static()
for i in range(100000): s.add(i)
static_time = time.time() - t1

t2 = time.time()
d = Dynamic()
for i in range(100000): d.add(i)
dynamic_time = time.time() - t2

print(f"Статический:  {static_time:.4f}с")
print(f"Динамический: {dynamic_time:.4f}с")
