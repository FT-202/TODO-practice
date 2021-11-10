set FLASK_APP=autoapp
set FLASK_DEBUG=1
flask db init
flask db migrate
flask db upgrade
flask run --with-threads
