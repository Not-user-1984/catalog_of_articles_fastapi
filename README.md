# catalog_of_articles_fastapi
### запуск
```
git clone git@github.com:Not-user-1984/catalog_of_articles_fastapi.git
cd docker
docker-compose up -d --build
```
### Документация 
Документация 
Ручки разделены для каждой сушности есть crud, orders,
через swagger и тестить.

```
http://localhost:8000/docs
```


### Админка
Без паролей, есть поиск и сортировки.

```
http://localhost:8000/admin/
```
<br>
<br>


При сборке уже сгенерировалась тестовые данные,
есть 
<br>
<br>


### регистрация

```
http://localhost:8000/auth/register

{
  "email": "test@testov",
  "password": "1234",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false,
  "username": "test"
}

```

### получение токена

```
http://127.0.0.1:8000/auth/jwt/login

в postman body > from-data
передать 
username = email # не много криво, но там былы задумка с расссылкой по email
password = password

```
<br>
<br>

### создание статьи

токен в запрос postman

```
http://127.0.0.1:8000/articles/

{
  "title": test",          # поля уникальные
  "description": "test",   # поля уникальные
  "link": "string3dd",
  "category_id": 1
}
