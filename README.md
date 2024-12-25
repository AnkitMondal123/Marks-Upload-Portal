# Marks Upload Portal

## 🚀 Features

- Django 5.1 & Python 3.12
- Installation via [Pip](https://pypi.org/project/pip/) or [Docker](https://www.docker.com/)
- User authentication--log in, sign up, password reset--via [django-allauth](https://github.com/pennersr/django-allauth)
- Static files configured with [Whitenoise](http://whitenoise.evans.io/en/stable/index.html)
- Styling with [Bootstrap v5](https://getbootstrap.com/)
- Debugging with [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
- DRY forms with [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
- Custom 404, 500, and 403 error pages

## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)
* [Next Steps](#next-steps)
* [Contributing](#contributing)


## 📖 Installation
Lithium can be installed via Pip or Docker. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/Anirban-Majumder/Marks-Upload-Portal.git
$ cd Marks-Upload-Portal
```

### Pip
You can use [pip](https://pypi.org/project/pip/) to create a fresh virtual environment on either Windows or macOS.

```
# On Windows
$ python -m venv .venv
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1
(.venv) $

# On macOS
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $
```

Then install all packages hosted in `requirements.txt` and run `migrate` to configure the initial database. The command `createsuperuser` will create a new superuser account for accessing the admin. Execute the `runserver` commandt o start up the local server.

```
(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000 or http://127.0.0.1:8000/admin for the admin
```

## Next Steps

- Add environment variables. There are multiple packages but I personally prefer [environs](https://pypi.org/project/environs/).
- Add [gunicorn](https://pypi.org/project/gunicorn/) as the production web server.
- Update the [EMAIL_BACKEND](https://docs.djangoproject.com/en/4.0/topics/email/#module-django.core.mail) and connect with a mail provider.
- Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure).
- `django-allauth` supports [social authentication](https://django-allauth.readthedocs.io/en/latest/providers.html) if you need that.


## 🤝 Contributing

Contributions, issues and feature requests are welcome! See [CONTRIBUTING.md]


