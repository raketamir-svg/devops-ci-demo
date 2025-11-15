# Базовый образ с Python
FROM python:3.9-slim

# Устанавливаем зависимости
RUN pip install flask

# Копируем код приложения
COPY app.py /app/app.py
WORKDIR /app

# Запускаем Flask-сервер
CMD ["python", "app.py"]
