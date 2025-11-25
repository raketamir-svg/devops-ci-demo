# ~/devops-mini-project/app3/Dockerfile
FROM python:3.9-slim
WORKDIR /app

# Копируем и устанавливаем зависимости
COPY requirements.txt .
# Критический шаг: установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копируем сам код приложения
COPY app.py .

CMD ["python", "app.py"]
