# STRIPE PAYMENTS API

## Стек технологий
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

## Системные требования
- Python 3.7+
- Docker
- Works on Linux, Windows, macOS

## Описание проекта
В проекте реализован Django + Stripe API бэкенд со следующим функционалом:
 - Django Модель Item с полями (name, description, price, currency) 
- API с двумя методами:
```
GET /buy/{id}
```
c помощью которого можно получить Stripe Session Id для оплаты выбранного Item.
```
GET /item/{id}
```
c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy происходит запрос на /buy/{id}, получение session_id и далее редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

Дополнительно реализованы Django-модели Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items и модель Discount.
В модель Item добавлено поле currency для двух разных валют, и в зависимости от валюты выбранного товара предлагается оплата в соответствующей валюте.

## Запуск проекта в контейнерах Docker
Клонируйте репозиторий и перейдите в него в командной строке.
Создайте и активируйте виртуальное окружение:
```
git clone https://github.com/Seniacat/stripe_payments_api
cd stripe_payments/
```
Cоздать и открыть файл .env с переменными окружения:
```
cd infra
touch .env
```
Заполнить .env файл с переменными окружения по примеру (SECRET_KEY см. в файле settings.py). 
Необходимые для работы проекта переменные окружения можно найти в файле .env.example в текущей директории:
```
echo DB_ENGINE=django.db.backends.postgresql >> .env

echo DB_NAME=postgres >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo POSTGRES_USER=postgres  >> .env

echo DB_HOST=db  >> .env

echo DB_PORT=5432  >> .env

echo SECRET_KEY=************ >> .env
```
Ввести значения публичного и приватного ключей STRIPE и адрес хоста 
```
echo STRIPE_PUBLIC_KEY=************ >> .env

echo STRIPE_SECRET_KEY=************ >> .env

echo DOMAIN=************ >> .env
```
Установить и запустить приложения в контейнерах:
```
docker-compose up -d
```
Запустить миграции, создать суперюзера, собрать статику и заполнить БД:
```
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input 
```
Если запуск приложения производится на удаленном сервере, внесите адрес хоста в файл настроек default.conf:
```
server {
    listen 80;
    server_name 127.0.0.1 <YOUR_DOMAIN>;
```
