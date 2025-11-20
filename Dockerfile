# --- ЭТАП 1: BUILDER (для установки зависимостей) ---
# ИСПРАВЛЕНИЕ: Переключаемся на Alpine для совместимости и минимального размера
FROM python:3.11-alpine AS builder 

# ... (остальные команды остаются прежними)
WORKDIR /app

COPY app-code/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- ЭТАП 2: FINAL (Финальный МИНИМАЛЬНЫЙ образ) ---
# ИСПРАВЛЕНИЕ: Финальный образ также на Alpine
FROM python:3.11-alpine

WORKDIR /app

# Копируем установленные зависимости из Этапа 1
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

CMD ["python", "/app/app.py"]
