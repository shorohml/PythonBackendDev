## Установка пакетов

```
sudo apt-get install -y nginx apache2-utils
```

## Запуск gunicorn

```
gunicorn --workers 4 myapp:app
```

## Запуск nginx

Добавить кусок из ./nginx.conf в /etc/nginx/nginx.conf, затем выполнить
```
sudo /etc/init.d/nginx start
```

### Параметры для отказа системы:

- отдача статических файлов (cat.jpg):
```
ab -n 10000 -c 2500 127.0.0.1:8080/static/cat.jpg
```
- отдача динамических документов Gunicorn:
```
ab -n 10000 -c 8200 127.0.0.1:8000/
```
- отдача динамических документов Gunicorn при проксировании через Nginx:
```
ab -n 10000 -c 450 127.0.0.1:8080/api
```