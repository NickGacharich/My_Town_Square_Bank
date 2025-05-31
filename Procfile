web: gunicorn My_Town_Square_Bank.wsgi:application --log-file - --log-level debug
heroku ps:scale web=1
manage.py migrate
