# guider-test-python


CREATE USER cities_user WITH PASSWORD 'password';

CREATE DATABASE cities_db WITH OWNER cities_user;

python manage.py migrate
