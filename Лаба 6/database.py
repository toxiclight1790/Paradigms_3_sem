import sqlite3

# Создание соединения с базой данных
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создание таблицы для хранения ответов пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_responses (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        location TEXT,
        favorite_color TEXT
    )
''')

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
