# Characterigy

После регистрации на сайте вы можете создавать листы персонажей для Dungeons and Dragons("создать"). Доступ к созданным персонажам вы можете получить на странице "мои персонажи".

http://51.15.97.72:8888/

Для создания листа персонажа необходимо указать класс и рассу. Эти параметры задают довольно много других параметров персонажа, поэтому в базе данных были организованы для них отдельные модели. В связи с этим, если запустить проект на своей машине, большая часть функционала будет недоступна.

## Чтобы запустить у себя
Клонируем репозиторий, активируем venv, устанавливаем django и psycopg2
```shellscript
git clone https://github.com/ris-iris/web_python_project.git
cd web_python_project
source env/bin/activate 
cd mysite
python -m pip install Django
pip install psycopg2
```
Организуем базу данных 
```shellscript
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo -u postgres createuser -s --superuser dndchardb
sudo -u postgres createdb dndchardb
sudo -u postgres psql -U postgres -d postgres -c "alter user postgres with password 'meowmeow';"
sudo adduser dndchardb
```
Имя superuser'а можно изменить на свое усмотрение, если изменяете название бд, user или passwor здесь
```shellscript
sudo -u postgres createdb dndchardb
sudo -u postgres psql -U postgres -d postgres -c "alter user postgres with password 'meowmeow';"
```
то их нужно изменить и в настройках (/mysite/mysite/settings.py, 81 - 83 строчка)

Запускаем проект
```shellscript
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
