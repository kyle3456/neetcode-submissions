class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num_elements = 0
        self.array = [0] * capacity
 
    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.num_elements >= self.capacity:
            self.resize()
        self.array[self.num_elements] = n
        self.num_elements += 1

    def popback(self) -> int:
        self.num_elements -= 1
        res = self.array[self.num_elements]
        return res

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(len(self.array)):
            new_array[i] = self.array[i]
        
        self.array = new_array


    def getSize(self) -> int:
        return self.num_elements
        
    
    def getCapacity(self) -> int:
        return self.capacity
