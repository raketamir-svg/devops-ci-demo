import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

DB_HOST = os.environ.get('DB_HOST', 'mysql')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'testdb')

@app.route('/')
def hello():
    try:
        # Пытаемся подключиться к MySQL
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        # Запрос версии
        cursor.execute("SELECT VERSION()")
        db_version = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        # Успешный результат
        return f"<h1>Hello from Flask (App3) - CI/CD VERSION 3!</h1><h2>✅ Connected to MySQL successfully. Version: {db_version}</h2>"

    except Exception as e:
        # Ошибка подключения или отсутствия библиотеки
        return f"<h1>Hello from Flask (App3)!</h1><h2>❌ Error: {e}</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
