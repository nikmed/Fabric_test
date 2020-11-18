#  Fabric_test

### Запуск
Для запуска Api необходимо иметь установленный докер.
Тогда запуск можно произвести с помощью комнад.
```sh
$ docker-compose up --build
```
После чего приложение будет запущено по адресу localhost:8000.

## Рутинг
### Вход от имени администратора
Для входа от имени администратора необходимо перейти на страницу
```sh
localhost:8000/admin
```
и ввести следующие данные.
```sh
login: admin
password: password
```

После авторизации администратор системы может просматривать/добавлять/изменять/удалять опросы. 
```sh
localhost:8000/api/poll/
localhost:8000/api/poll/<int:id>
```
Параметры для POST запроса
```sh
{
    "name": "Poll",
    "start_date": "2020-11-18",
    "end_date": "2020-11-21",
    "description": "Description"
}
```
И просматривать/добавлять/изменять/удалять вопросы для каждого опроса.
```sh
localhost:8000/api/question/
localhost:8000/api/question/<int:id>
```
Параметры для POST запроса
```sh
{
    "text": "Text",
    "question_type": "TXT",
    "poll": 1
}
```
Для поля "question_type" существует три варианта которые представлены ниже.
```sh
QUESTION_TYPE_CHOICES = [
	('TXT', 'Text answer'), 
	('POA' , 'Pick one answer'), 
	('PMA' , 'Pick multiple answer'),
	]
```
### Функционал для пользователя системы
Пользователь системы может просматривать активные опросы.
```sh
localhost:8000/api/active_poll/
```
Проходить опросы с помощью.
```sh
localhost:8000/api/answer/
```
Параметры для POST запроса
```sh
{
    "user_id": 1,
    "question_id": 4,
    "answer": "Answer"
}
```
И просматривать ответы с помощью.
```sh
localhost:8000/api/answer/<int:user_id>
```

