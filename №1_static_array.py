class Array_Edit:
# трудоёмскость оценивается по отношению к самому этому заданию

    def __init__(self):
        self.array=[2345,'4342', 543]

    # сложность 1/10
    def pushBack(self,value):
        self.array.append(value)
       
    # сложность 1/10
    def pushFront(self,value):
        self.array.insert(0, value) 

    # сложность 3/10
    def insert(self,index, value):
        if 0 <= index < len(self.array):
            self.array[index]= value
        else:
            self.array.append(value)

    # сложность 3/10
    def remove(self,index):
        if 0 <= index < len(self.array):
             self.array.pop(index) 
        else:
            print("Индекс вне диапазона")

        
    # сложность 5/10
    def find(self,value):
        try:
            return self.array.index(value)
            
        except ValueError:
            print("такого нет")
            return -1
         


if __name__ == '__main__':
    arr = Array_Edit()

    arr.pushBack(value=input('Введите значение для добавления в конец: '))
    arr.pushFront(value=input('Введите значение для добавления в начало: '))
    arr.insert(index=int(input('Введите индекс нового элемента: ')),value=input('Введите значение нового элемента: '))
    print(arr.array) 
    arr.remove(index=int(input('Введите индекс для удаления: ')))
    print(arr.array)
    index=arr.find(value=input('Введите значение для поиска: ')) 
    print(index)
