lightly modified from https://github.com/mitsuhiko/flask-sqlalchemy/tree/master/examples

## Dev setup

    $ export FLASK_APP=todo.py
    $ export TODO_SETTINGS=/path/to/local/config.cfg
    $ export FLASK_DEBUG=1
    $ flask run

## Database migrations

### Create a new migration

    $ flask db revision "revision comment"

### Apply db migrations

    $ flask db upgrade
