import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'grub.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Db
    from . import db
    db.init_app(app)

    # Orders
    from . import orders
    app.register_blueprint(orders.bp)
    app.add_url_rule('/', endpoint='index')

    # Orders
    from . import users
    app.register_blueprint(users.bp)

    return app