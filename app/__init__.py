import os, re

from flask import (
    Flask, request, render_template, flash
)

from flask_wtf.csrf import (
    CSRFProtect, CSRFError
)

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True, template_folder="templates")
    app.config.from_mapping(
        SECRET_KEY="dev"
    )

    CSRFProtect(app)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    from .r import bp as r_bp
    app.register_blueprint(r_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return e, 404

    return app