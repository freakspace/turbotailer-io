# Turbotailer

Turbotailer

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Prepare git

 - While logged in ubuntu 22

### Step 1 ###
 $ git --version
 $ sudo apt update
 $ sudo apt upgrade
 $ sudo apt install git
 $ git config --global user.name "YOUR NAME"
 $ git config --global user.email "YOUR GITHUB USERNAME"

### Step 2 ###

 $ ssh-keygen
 $ cat ~/.ssh/id_rsa.pub

### Step 3 ###

 - Copy the SSH key and add to your github account
 - Clone the github repositoy


## Prepare docker


- Make the script executable:

      $ chmod +x prepare_docker.sh

- Execute the script with:

      $ ./prepare_docker.sh


## Running docker first time

### In production ###
      $ sudo docker compose -f production.yml build
      $ sudo docker compose -f production.yml run --rm django python manage.py migrate
      $ sudo docker compose -f production.yml run --rm django python manage.py createsuperuser
      $ sudo docker compose -f production.yml up

### In staging ###
      $ sudo docker compose -f stage.yml build
      $ sudo docker compose -f stage.yml run --rm django python manage.py migrate
      $ sudo docker compose -f stage.yml run --rm django python manage.py createsuperuser
      $ sudo docker compose -f stage.yml up

### Locally ###
      $ docker compose -f local.yml build
      $ docker compose -f local.yml run --rm django python manage.py migrate
      $ docker compose -f local.yml run --rm django python manage.py createsuperuser
      $ docker compose -f local.yml up



## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy turbotailer

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd turbotailer
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd turbotailer
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd turbotailer
celery -A config.celery_app worker -B -l info
```

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

### Custom Bootstrap Compilation

The generated CSS is set up with automatic Bootstrap recompilation with variables of your choice.
Bootstrap v5 is installed using npm and customised by tweaking your variables in `static/sass/custom_bootstrap_vars`.

You can find a list of available variables [in the bootstrap source](https://github.com/twbs/bootstrap/blob/v5.1.3/scss/_variables.scss), or get explanations on them in the [Bootstrap docs](https://getbootstrap.com/docs/5.1/customize/sass/).

Bootstrap's javascript as well as its dependencies are concatenated into a single file: `static/js/vendors.js`.
