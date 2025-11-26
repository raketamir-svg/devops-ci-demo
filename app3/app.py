import os
import mysql.connector
from flask import Flask
from flask import jsonify

app = Flask(__name__)

# Новый эндпоинт для Liveness и Readiness Probes
@app.route('/healthz')
def health_check():
    return "OK", 200


# --- Конфигурация DB через переменные окружения (DevOps-стандарт) ---
# DB_HOST будет именем сервиса MySQL в Docker Compose!
DB_HOST = os.environ.get('DATABASE_HOST', 'mysql-db')
DB_USER = os.environ.get('DB_USER', 'root')
DB_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'password')
DB_NAME = os.environ.get('DB_NAME', 'testdb')

@app.route('/')
def hello():
    try:
        # 1. Подключение к MySQL
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        # 2. Выполнение простого запроса (получаем версию)
        cursor.execute("SELECT VERSION()")
        db_version = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        # 3. Возвращаем результат
        return f"<h1>Hello from Flask (App3)!</h1><h2>✅ Подключено к MySQL успешно. Версия: {db_version}</h2>"

    except Exception as e:
        # 4. Обработка ошибки, если не удалось подключиться
        return f"<h1>Hello from Flask (App3)!</h1><h2>❌ Ошибка подключения к MySQL: {e}</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
