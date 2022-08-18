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
(note: you may want to look at [Optional](#-optional) before starting the local server) 
* `py manage.py runserver`
<br />
...And done!

### NOTE
Its important to generate (or choose) your own `SECRET_KEY` located in `settings.py`, and not use the one already given.

# Optional
If you wish to be able to send email (using the button only certain admins can see/use), do the following:
* Create a (free, no billing) [mailgun account](https://signup.mailgun.com/new/signup)
* Navigate to `Sending > Domains` and click your (sandbox)domain
* Select `API`, and copy the `API key` and `API base URL`
* Go into `views.py` and find the function named `sendmail` located in the `# mail` section
* Paste the key and base url into the relevent places

<br>

If you wish to not see detailed error messages when something goes wrong, do the following:
* Go into `settings.py` located in the `project` folder, and set `DEBUG=False`
* In the same file, add `['*']` to `ALLOWED_HOSTS`
(note: in production you want to set ALLOWED_HOSTS to something like `['.herokuapp.com', 'localhost', '127.0.0.1']`)
