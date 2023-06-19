import psycopg2

# Подключение к серверу PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="postgres"
)

# Создание базы данных
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE organiser")
cur.close()
conn.close()

# Подключение к созданной базе данных
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="postgres",
    database="organiser"
)

# Создание таблицы
cur = conn.cursor()
create_table_query = '''
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    description TEXT,
    deadline TIMESTAMP,
    completed BOOLEAN,
    recurring TEXT
)
'''
cur.execute(create_table_query)
cur.close()
conn.close()