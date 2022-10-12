# Task 1
from dataclasses import dataclass
from abc import ABC


@dataclass
class Film(ABC):
    name: str
    country: str
    director: str
    genre: str
    time: int


class Show:

    def __init__(self, _film):
        self.film = _film

    def show_film(self):
        print(f'Name is {self.film.name}')
        print(f'Country is {self.film.country}')
        print(f'Director is {self.film.director}')
        print(f'Genre is {self.film.genre}')
        print(f'Time is {self.film.time} minutes\n')


film_1 = Film(
    name='Harry Potter',
    country='Great Britain and USA',
    director='Chris Columbus',
    genre='fantasy',
    time=152
)

film_2 = Film(
    name='Home Alone',
    country='USA',
    director='Chris Columbus',
    genre='comedy',
    time=103
)

f_1 = Show(film_1)
f_1.show_film()

f_2 = Show(film_2)
f_2.show_film()


# Task 2
class Static:
    name = 'Elizaveta'

    def method_1(self):
        print(f'My name is {self.name}')

    @staticmethod
    def method_2():
        print('My name is Liza\n')


st = Static()
st.method_1()

Static.method_2()


# Task 3
class Class:
    age = 19

    def method_1(self):
        print(f'My age is {self.age}')

    @classmethod
    def method_2(cls):
        print('My surname is Selitskaya')


Class.method_2()
cl = Class()
cl.method_1()
