Запуск веб-платформы для знакомств

Требования
- Python 3.x
- Docker и Docker Compose
- PostgreSQL

Шаги по запуску

1. **Клонируйте репозиторий**:
git clone <URL>
cd <repository_name>

2.Создайте файл .env и заполните его данными для подключения к базе данных:
POSTGRES_DB=dataproject
POSTGRES_USER=Mitya
POSTGRES_PASSWORD=Baburin17!   

3.Соберите контейнеры:
docker-compose build

4.Запустите приложение:
docker-compose up

5.Выполните миграции (в другом терминале):
docker-compose exec web python manage.py migrate

6.Запустите тесты (при необходимости):
docker-compose exec web python manage.py test

7.Откройте браузер и перейдите по адресу:
http://localhost:8000
