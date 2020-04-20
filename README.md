# aipos3
## Установка virtual environment
1) в папке с проектом через консоль вводим python -m venv env
2) вводим source env/bin/activate
3) устанавливаем рекомендации в корне проекта вводим pip install -r requirements.txt
## Настройки бд
1) в файле app/\_\_init\_\_.py подставить свои данные в строке app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://name_user:password@localhost/name_db'
2) в корне проекта вводим export FLASK_APP=db.py
3) python -m flask db init
4) python -m flask db migrate
5) python -m flask db upgrade

Готово, запускаем проект python -m flask run и заходим http://127.0.0.1:5000/
## URLs
+ /conference - таблица со всеми conferences, здесь же и удаление 
+ /conference/add - добавление записи
+ /conference/<id_conf> - просмотр информации и изменение информации отдельного объекта по его id
***
+ /room - таблица со всеми rooms, здесь же и удаление
+ /room/add - добавление записи
+ /room/<id_room> - просмотр информации и изменение информации отдельного объекта по его id
***
+ /paper - таблица со всеми papers, здесь же и удаление
+ /paper/add - добавление записи
+ /paper/<id_paper> - просмотр информации и изменение информации отдельного объекта по его id
***
+ /presentation - таблица со всеми presentation_times, здесь же и удаление
+ /presentation/add - добавление записи
+ /presentation/<id_presentation> - просмотр информации и изменение информации отдельного объекта по его id
***
+ /tag - таблица со всеми tags, здесь же и удаление
+ /tag/add - добавление записи
+ /tag/<id_tag> - просмотр информации и изменение информации отдельного объекта по его id
***
+ /user - таблица со всеми users, здесь же и удаление
+ /user/add - добавление записи
+ /user/<id_user> - просмотр информации и изменение информации отдельного объекта по его id
# Описание архитетктуры
1) файл rest.py выступает в роли сервера, который получает запросы с клиента
+ написаны для каждой сущности методы get_all_\*, get_\*, delete_\*, update_\*, add_*, где * название сущности
2) файл view.py выступает в роли клиента, который принимает запросы
+ написаны для каждой сущности методы all_\*, delete_\*, edit_\*, add_*, где * название сущности
3) файл \_\_init\_\_.py содержит все настройки проекта
4) в папке templates хранятся шаблоны html
5) в файле models.py хранится описание каждой сущности, по которому генерируются таблицы в бд
