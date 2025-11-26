# app2/Dockerfile

# 1. Используем официальный образ Node.js (вместо Nginx)
FROM node:20-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# 2. Копируем файл приложения (предполагаем, что он называется server.js)
# Если у вас есть package.json, вам также нужно его скопировать и выполнить npm install
COPY server.js /app/server.js

# Открываем порт 80
EXPOSE 80

# 3. Запускаем Node.js приложение (этот шаг был пропущен)
CMD ["node", "server.js"]
