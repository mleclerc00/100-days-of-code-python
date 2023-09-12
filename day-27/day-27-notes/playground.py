from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Union

# args example
def add(*args: int) -> int:
    sum = 0
    for i in args:
        sum += i
    return sum
        

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# kwargs example
def calculate(n: int, **kwargs: int):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    

calculate(2, add=3, multiply=5)

# kwargs example 2
class Car:
    def __init__(self, **kwargs: Union[str, int]):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.color = kwargs.get('color')
        self.seats = kwargs.get('seats')

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)