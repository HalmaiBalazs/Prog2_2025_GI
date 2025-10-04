from functools import total_ordering

class Drink:
    name: str
    _size: str
    __price: int

    def __init__(self, name: str, size: str, price: int):
        self.name = name
        self._size = "5 dl"
        self.__price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size: str):
        self._size = size

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: int):
        self.__price = price

    def __repr__(self):
        return f"Drink({self.name}, {self.size}, {self.price})"

    def __str__(self):
        return f"Drink({self.name}, {self.size}, {self.price} Ft)"

    def __eq__(self, other):
        return self._size == other._size and self.__price == other.__price and self.name == other.name

    def __lt__(self, other):
        return self._size > other._size or self.__price < other.__price and self.name > other.name

