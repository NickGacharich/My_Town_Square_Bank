web:gunicorn my_town_square_bank.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
