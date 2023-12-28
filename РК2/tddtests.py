import unittest
from main import *


class TestRK2(unittest.TestCase):
    # Магазины
    storees = [
        City_store(1, 'Ходасевич'),
        City_store(2, 'Пушкинская лавка'),
        City_store(3, 'Гиперион'),

        City_store(11, 'Художественная литература'),
        City_store(22, 'Фаланстер'),
        City_store(33, 'Циолковский'),
    ]

    # Книги
    books = [
        Book(1, 'Оно', 1138, 1),
        Book(2, 'Преступление и наказание', 574, 1),
        Book(3, 'Гамлет', 300, 2),
        Book(4, 'Убийство в Восточном экспрессе', 317, 2),
        Book(5, 'Молчание ягнят', 496, 3),
    ]

    def test_A1(self):
        one_to_many = [(p.name, p.nop, c.name)
                       for c in storees
                       for p in books
                       if p.store_id == c.id]
        self.assertEqual(a1_solution(one_to_many),
                         [('Молчание ягнят', 496, 'Гиперион'), ('Гамлет', 300, 'Пушкинская лавка'),
                           ('Убийство в Восточном экспрессе', 317, 'Пушкинская лавка'), ('Оно', 1138, 'Ходасевич'), ('Преступление и наказание', 574, 'Ходасевич')])

    def test_A2(self):
        one_to_many = [(p.name, p.nop, c.name)
                       for c in storees
                       for p in books
                       if p.store_id == c.id]
        self.assertEqual(a2_solution(one_to_many),
                         [('Ходасевич', 1712), ('Пушкинская лавка', 617), ('Гиперион', 496)])

    def test_A3(self):
        many_to_many_temp = [(c.name, pc.store_id, pc.book_id)
                             for c in storees
                             for pc in books_storees
                             if c.id == pc.store_id]

        many_to_many = [(p.name, p.nop, store_name)
                        for store_name, store_id, book_id in many_to_many_temp
                        for p in books if p.id == book_id]
        self.assertEqual(a3_solution(many_to_many),
                         {'Ходасевич': ['Оно', 'Преступление и наказание'],
                           'Художественная литература': ['Оно', 'Молчание ягнят']})


if __name__ == '__main__':
    unittest.main()