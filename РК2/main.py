# используется для сортировки
from operator import itemgetter


# Класс "книга"
class Book: 
    def __init__(self, id, name, nop, store_id):
        self.id = id
        self.name = name
        self.nop = nop
        self.store_id = store_id


# Класс "книжный магазин"
class City_store:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookStore:
    def __init__(self, store_id, book_id):
        self.store_id = store_id
        self.book_id = book_id


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

books_storees = [
    BookStore(1,1),
    BookStore(1,2),
    BookStore(2,3),
    BookStore(2,4),
    BookStore(3,5),

    BookStore(11,1),
    BookStore(11,2),
    BookStore(22,3),
    BookStore(22,4),
    BookStore(33,5),
]


def a1_solution(one_to_many):
    res_11 = sorted(one_to_many, key=itemgetter(2))
    return res_11


def a2_solution(one_to_many):
    res_12_unsorted = []

    for c in storees:

        c_books = list(filter(lambda i: i[2] == c.name, one_to_many))

        if len(c_books) > 0:

            c_nops = [sal for _, sal, _ in c_books]

            c_nops_sum = sum(c_nops)
            res_12_unsorted.append((c.name, c_nops_sum))

    # Сортировка по сумме ядер
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    return res_12


def a3_solution(many_to_many):
    res_13 = {}

    for c in storees:
        if 'Х' in c.name:

            c_books = list(filter(lambda i: i[2] == c.name, many_to_many))

            c_books_names = [x for x, _, _ in c_books]
            # Добавляем результат в словарь
            # ключ - магазинов, значение - список названий книг
            res_13[c.name] = c_books_names
    return res_13


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(p.name, p.nop, c.name)
                   for c in storees
                   for p in books
                   if p.store_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, pc.store_id, pc.book_id)
                         for c in storees
                         for pc in books_storees
                         if c.id == pc.store_id]

    many_to_many = [(p.name, p.nop, store_name)
                    for store_name, store_id, book_id in many_to_many_temp
                    for p in books if p.id == book_id]

    print('Задание А1')
    print(a1_solution(one_to_many))

    print('\nЗадание А2')
    print(a2_solution(one_to_many))

    print('\nЗадание А3')
    print(a3_solution(many_to_many))


if __name__ == '__main__':
    main()

# Результаты выполнения:
#
# Задание А1
# [('Pentium', 2, 'ASUS 2000'), ('Celeron', 1, 'ASUS 2000'), ('Core i3', 4, 'Honor 2020'), ('Core i7', 2, 'Honor 2020'), ('M1', 8, 'MacBook Pro')]
#
# Задание А2
# [('MacBook Pro', 8), ('Honor 2020', 6), ('ASUS 2000', 3)]
#
# Задание А3
# {'MacBook Air': ['Pentium', 'Celeron', 'Core i3'], 'MacBook Pro': ['M1'], 'iMac 2013': ['Core i7']}