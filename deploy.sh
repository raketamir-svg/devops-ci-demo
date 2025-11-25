#!/bin/bash

# --- КОНФИГУРАЦИЯ ---
# !!! ОБЯЗАТЕЛЬНО ЗАМЕНИТЕ "olegxxx1" НА ВАШ ЛОГИН DOCKER HUB !!!
DOCKER_USER="olegxxx1" 
IMAGE_NAME="${DOCKER_USER}/devops-mini-project-app3"
CHART_PATH="./devops-mini-project-chart"
RELEASE_NAME="my-project"
TAG="latest" 

echo "--- Шаг 1: Сборка нового Docker образа App3 ---"
# Собираем Docker образ из папки app3, используя ее как контекст
# Мы используем Dockerfile, который находится внутри папки app3
docker build -t ${IMAGE_NAME}:${TAG} -f ./app3/Dockerfile ./app3

# Проверяем успешность сборки
if [ $? -ne 0 ]; then
    echo "ОШИБКА: Сборка образа App3 завершилась неудачно."
    exit 1
fi

echo "--- Шаг 2: Отправка образа в Docker Hub ---"
docker push ${IMAGE_NAME}:${TAG}

echo "--- Шаг 3: Обновление Helm Chart в Minikube ---"
# Обновляем Helm Chart, явно передавая новый тег образа, 
# чтобы Kubernetes выполнил Rollout (перезапуск Pod'ов с новым образом)
helm upgrade ${RELEASE_NAME} ${CHART_PATH} \
    --set app3.image="${IMAGE_NAME}:${TAG}"

echo "--- Развертывание Helm завершено! Проверка статуса ---"
kubectl get all | grep ${RELEASE_NAME}

echo "--- Проверьте работу системы: curl http://$(minikube ip):30080 ---"
