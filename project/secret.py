from flask import Blueprint, render_template
from project.auth import login_required

bp = Blueprint('secret', __name__)


@bp.route('/')
@login_required
def secret():
    return render_template("secrets.html")
