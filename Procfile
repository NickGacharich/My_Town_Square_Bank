web: gunicorn my_town_square_bank.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
manage.py migrate
