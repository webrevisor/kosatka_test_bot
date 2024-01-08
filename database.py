import sqlite3

# Подключение к базе данных SQLite (база данных будет создана, если она не существует)
conn = sqlite3.connect('telegram.db')

# Создание курсора
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS last_messages (
        account_name VARCHAR(255),
        channel_id INTEGER,
        message_id INTEGER,
        UNIQUE(account_name, channel_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mapped_messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_name VARCHAR(255),
        source_channel_id INTEGER,
        source_message_id INTEGER,
        target_channel_id INTEGER,
        target_message_id INTEGER,
        UNIQUE (account_name, source_channel_id, source_message_id, target_channel_id)
    )
''')

# Сохранение изменений и закрытие соединения
conn.commit()


def get_mapped_message_by(account_name, source_channel_id, source_message_id, target_channel_id):
    cursor.execute('''
        SELECT * FROM mapped_messages WHERE
        account_name=? AND
        source_channel_id=? AND
        source_message_id=? AND
        target_channel_id=?
    ''', (account_name, source_channel_id, source_message_id, target_channel_id))

    mapped_message = cursor.fetchone()

    return mapped_message


def delete_mapped_message(account_name, source_channel_id, source_message_id, target_channel_id, target_message_id):
    cursor.execute('''
        DELETE FROM mapped_messages WHERE
        account_name=? AND
        source_channel_id=? AND
        source_message_id=? AND
        target_channel_id=? AND
        target_message_id=?
    ''', (account_name, source_channel_id, source_message_id, target_channel_id, target_message_id))
    conn.commit()


def get_count_mapped_messages(account_name, source_channel_id):
    response = cursor.execute('''
        SELECT COUNT(*) FROM mapped_messages WHERE account_name=? AND source_channel_id=?
    ''', (account_name, source_channel_id))
    return response.fetchone()[0]


def insert_mapped_message(account_name, source_channel_id, source_message_id, target_channel_id, target_message_id):
    cursor.execute('''
        INSERT INTO mapped_messages (account_name, source_channel_id, source_message_id, target_channel_id, target_message_id)
        VALUES (?, ?, ?, ?, ?)
    ''', (account_name, source_channel_id, source_message_id, target_channel_id, target_message_id))
    conn.commit()


def insert_last_message(account_name, channel_id, message_id):
    cursor.execute('''
           INSERT OR REPLACE INTO last_messages (account_name, channel_id, message_id)
           VALUES (?, ?, ?)
       ''', (account_name, channel_id, message_id))
    conn.commit()


def get_last_messages_by_acc(account_name):
    response = cursor.execute('''SELECT * FROM last_messages where account_name=?''', (account_name,))
    return response.fetchall()


def get_last_messages_by_channel(channel_id):
    response = cursor.execute('''SELECT * FROM last_messages where channel_id=?''', (channel_id,))
    return response.fetchone()


def remove_mapped_messages(ids):
    placeholder = '?'  # For SQLite. See DBAPI paramstyle.
    placeholders = ', '.join(placeholder for unused in ids)
    cursor.execute('DELETE FROM mapped_messages WHERE id IN (%s)' % placeholders, ids)
    conn.commit()


def get_mapped_messages_by_acc_channel(account_name, channel_id, target_id):
    response = cursor.execute('''SELECT id FROM mapped_messages where account_name=? and source_channel_id=? and target_channel_id=?''',
                              (account_name, channel_id, target_id))
    return response.fetchall()
