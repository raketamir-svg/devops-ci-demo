# 1. FROM — базовый образ
FROM nginx:latest


# Удаление стандартной конфигурации Nginx, которая конфликтует
RUN rm /etc/nginx/conf.d/default.conf

# 2. COPY — копируем наш конфиг внутрь контейнера
COPY nginx.conf /etc/nginx/conf.d/balancer.conf

# 3. EXPOSE — открываем порт для доступа снаружи
EXPOSE 80
