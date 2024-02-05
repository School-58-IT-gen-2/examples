# Docker
Создание образа
docker build -t image_name:{TAG} .

Загрузка образа
docker pull image_name:{TAG}

Сохранение в архив
docker save image_name:{TAG} -o image_name.tar

Загрузка из архива
docker load < image_name.tar

# Docker Compose
Запуск композиции контейнеров
docker-compose up

"Тихий" запуск композиции контейнеров
docker-compose up -d

Остановка композиции контейнеров
docker-compose down