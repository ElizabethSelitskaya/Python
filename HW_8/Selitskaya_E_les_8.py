# Task №1
import time

class Auto:
    brand = 'Ferrari'
    age = 4
    color = 'black'
    mark = '458'
    weight = 1380

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        age = Auto.age + 1
        print(f'age is {age}')

# Task №2
class Truck(Auto):
    max_load = 3

    def move(self):
        print('attention')
        return super().move()

    def load(self):
        print('load')
        time.sleep(1)


class Car(Auto):
    max_speed = 325

    def move(self):
        print(f'max speed is {Car.max_speed}')


auto1 = Auto()
truck1 = Truck()
car1 = Car()

print(f'brand is {auto1.brand}')
print(f'color is {auto1.color}')
print(f'mark is {auto1.mark}')
print(f'weight is {auto1.weight}')
auto1.move()
auto1.stop()
auto1.birthday()

print(f'max load is {truck1.max_load}')
truck1.move()
truck1.load()

car1.move()
