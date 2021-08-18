# Описание проекта
REST API для сервиса отзывов о фильмах, книгах и музыке.

## Начало работы

Для начала работы клонируйте репозиторий:

```
git clone <адрес репозитория>
```

Для работы с проектом у вас должен быть установлен Docker и docker-compose. Данная команда скачает скрипт для установки докера:

```
curl -fsSL https://get.docker.com -o get-docker.sh
```

Следующая команда запустит его:

```
sh get-docker.sh
```

Установка docker-compose:

```
apt install docker-compose
```

## Установка

В локальном репозитории перейдите в каталог проекта и выполните команду:

```
docker-compose up
```

После сборки контейнера перейдите в запущенный контейнер и выполните миграции:

```
sudo docker-compose exec web python manage.py makemigrations api --noinput
sudo docker-compose exec web python manage.py migrate api --noinput
```

Для использования панели администратора по адресу http://127.0.0.1/admin/ необходимо создать суперпользователя:

```
python manage.py createsuperuser.
```

Собираем статику:

```
sudo docker-compose exec web python manage.py collectstatic --no-input
```

Для загрузки в БД тестовых данных используйте файл fixtures.json из корневой папки проекта:

```
docker cp fixtures.json <CONTAINER ID>:/code/fixtures.json
```

Перейдите в контейнер приложения и загрузите данные в БД:

```
docker container exec -it <CONTAINER ID> bash
python manage.py loaddata fixtures.json
```

## Бейдж
https://github.com/octomckelpo/yamdb_final/workflows/yamdb_workflow.yaml/badge.svg

## Развернутый проект можно посмотреть по ссылке:
http://84.201.139.232/api/v1/