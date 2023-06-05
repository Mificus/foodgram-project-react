# Foodgram React

[![Foodgram workflow](https://github.com/Mificus/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/Mificus/foodgram-project-react/actions/workflows/main.yml)

## Описание
приложение «Продуктовый помощник»: сайт, на котором пользователи будут публиковать
рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других а
второв. Сервис «Список покупок» позволит пользователям создавать список продуктов, 
которые нужно купить для приготовления выбранных блюд. 

На этом сервисе пользователи смогут публиковать рецепты, 
подписываться на публикации других пользователей, добавлять понравившиеся рецепты 
в список «Избранное», а перед походом в магазин скачивать сводный список 
продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Доступ

Проект запущен на сервере и доступен по адресам:
- http://50.52.25.26/recipes
- Админ-зона: http://50.52.25.26/admin
Логин - Maksim
Пароль - Lastochkin 

- API: http://50.52.25.26/admin
 
## Стек технологий
- Python
- Django 3.2
- DRF
- PostgreSQL
- Docker
- Github Actions


## Для запуска на собственном сервере:
1. Скопируйте из репозитория файлы, расположенные в директории infra:
    - docker-compose.yml
    - nginx.conf
2. В директории foodgram создайте директорию infra и поместите в неё файлы:
    - docker-compose.yml
    - nginx.conf
    - .env (пустой)
3. Файл .env должен быть заполнен следующими данными:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

4. В директории infra следует выполнить команды:
```
sudo docker-compose up -d
sudo docker-compose exec backend python manage.py makemigrations
sudo docker-compose exec backend python manage.py migrate
sudo docker-compose exec backend python manage.py collectstatic --no-input
```

5. Для создания суперпользователя, выполните команду:
```
docker-compose exec backend python manage.py createsuperuser
```

6. Для добавления ингредиентов в базу данных, выполните команду:
```
sudo docker-compose exec backend python manage.py commands
```
После выполнения этих действий проект будет запущен в трех контейнерах (backend, db, nginx) и доступен по адресам:

- Главная страница: http://<ip-адрес>/recipes/
- API проекта: http://<ip-адрес>/api/
- Admin-зона: http://<ip-адрес>/admin/
7. Теги вручную добавляются в админ-зоне в модель Tags;
8. Проект запущен и готов к регистрации пользователей и добавлению рецептов.

### Автор
Ласточкин Максим
