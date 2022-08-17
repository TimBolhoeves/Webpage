# Webstore django training
A webpage application made to train some of the more complex Django stuff.

# Setup
To setup and run this application follow these steps in-order.
* `py -m venv .venv`
* `.\.venv\Scripts\activate` (and select the interpreter in your IDE (VScode = f1>select interpreter))
* `py -m pip install -r requirements.txt`
* `py manage.py makemigrations`
* `py manage.py migrate`
* `py manage.py createsuperuser` and follow the steps
* `py manage.py runserver`
<br>
...And done!

# Optional
If you wish to not see detailed error messages when something goes wrong, do the following:
* Go into `settings.py` located in the `project` folder, and set `DEBUG=False`
* In the same file, add `['*']` to `ALLOWED_HOSTS`
(note: in production you want to set ALLOWED_HOSTS to something like `['.herokuapp.com', 'localhost', '127.0.0.1']`)