import sqlite3

# Подключение к базе данных SQLite (база данных будет создана, если она не существует)
conn = sqlite3.connect('telegram.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS last_messages (
        channel_id INTEGER,
        message_id INTEGER,
        UNIQUE(channel_id)
    )
''')

# Сохранение изменений и закрытие соединения
conn.commit()
