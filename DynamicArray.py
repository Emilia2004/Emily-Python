class DynamicArray:
    def __init__(self, capacity: int = 10):
        self.__size = 0  
        self.__capacity = capacity 
        self.__array = self.make_array(self.__capacity)

    def __len__(self) -> int:
        return self.__size

    def __getitem__(self, index: int) -> any:
        if -1*(self.__size) <= index < self.__size :
            return self.__array[index]
        raise IndexError

    def __setitem__(self, index: int, value: any) -> None:
        if -1*(self.__size) <= index < self.__size:
            self.__array[index] = value
        else:
            raise IndexError

    def append(self, element: any) -> None:
        if self.__size == self.__capacity:
            self._resize(2 * self.__capacity)  
        self.__array[self.__size] = element
        self.__size += 1

    def _resize(self, new_capacity: int) -> None:
        new_array = self.make_array(new_capacity)
        for i in range(self.__size):
            new_array[i] = self.__array[i]
        self.__array = new_array
        self.__capacity = new_capacity

    def make_array(self, capacity: int):
        return capacity * [0]

    def __str__(self) -> str:
        return str([self.__array[i] for i in range(self.__size)])

    def __repr__(self) -> str:
        return f"DynamicArray({[self.__array[i] for i in range(self.__size)]})"


    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        if not isinstance(other, DynamicArray):
            raise TypeError("Can't support + operator for not Dynamicarray type")
        new_array = DynamicArray(self.__size + other.__size)
        for i in range(self.__size):
            new_array.append(self.__array[i])
        for i in range(other.__size):
            new_array.append(other.__array[i])
        return new_array

    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        if not isinstance(other, DynamicArray):
            raise TypeError("Can't support + operator for not Dynamicarray type")
        for i in range(other.__size):
            self.append(other.__array[i])
        return self

    def __eq__(self, other: 'DynamicArray') -> bool:
        if not isinstance(other, DynamicArray):
            return False
        if self.__size != other.__size:
            return False
        for i in range(self.__size):
            if self.__array[i] != other.__array[i]:
                return False
        return True

    def __ne__(self, other: 'DynamicArray') -> bool:
        return not self.__eq__(other)

    def __lt__(self, other: 'DynamicArray') -> bool:
        return list(self) < list(other)

    def __le__(self, other: 'DynamicArray') -> bool:
        return list(self) <= list(other)

    def __gt__(self, other: 'DynamicArray') -> bool:
        return list(self) > list(other)

    def __ge__(self, other: 'DynamicArray') -> bool:
        return list(self) >= list(other)

    def __iter__(self):
        for i in range(self.__size):
            yield self.__array[i]

    def __hash__(self):
        raise TypeError("DynamicArray cannot be hashed")
    

