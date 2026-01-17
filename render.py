from flask import Blueprint, render_template

ui_bp = Blueprint('render_ui', __name__, url_prefix='/file-transfer')

@ui_bp.route("/main", methods=["GET"])
def render_mainpage():
    return render_template("index.html")
