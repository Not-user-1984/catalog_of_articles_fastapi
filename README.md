# catalog_of_articles_fastapi
### запуск
```
git clone git@github.com:Not-user-1984/catalog_of_articles_fastapi.git
cd docker
docker-compose up -d --build
```
### Документация 
Документация 


```
http://127.0.0.1:8000/docs
```


### Админка
Без паролей, есть поиск и сортировки.

```
http://127.0.0.1t:8000/admin/
```
<br>
<br>


При сборке уже сгенерировалась тестовые данные 
<br>
<br>


### регистрация

```
http://127.0.0.1:8000/auth/register

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
username = email # немного криво, но там былы задумка с расссылкой по email
password = password

```
<br>
<br>

### создание статьи

токен в запрос postman

```
http://127.0.0.1:8000/articles/

{
  "title": test",          # полe уникальнoe
  "description": "test",   # полe уникальнoe
  "link": "string3dd",
  "category_id": 1
}
```


### другие запросы 
токен в запрос postman

```
get
http://127.0.0.1:8000/articles/?limit=2 
все статьи с лимитом

get
http://127.0.0.1:8000/article_categories/
все категории

post
http://127.0.0.1:8000/article_categories/
создать категорию
{
  "name": "test"  # полe уникальнoe
}

остальные put, delete
можно посмотреть 
http://127.0.0.1:8000/docs
```
