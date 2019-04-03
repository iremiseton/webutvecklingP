from flask import (
    redirect, render_template, url_for, flash
)

from . import bp

@bp.route("/", methods=('GET', 'POST'))
def index():
    return render_template("app/index.html")