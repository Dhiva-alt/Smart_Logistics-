from flask import Blueprint
from controllers.auth_controller import login, protected
from controllers.auth_controller import (
login,
protected,
admin_panel
)

auth_bp = Blueprint("auth", __name__)

auth_bp.route('/login', methods=['POST'])(login)

auth_bp.route('/protected', methods=['GET'])(protected)
auth_bp.route(
'/admin',
methods=['GET']
)(admin_panel)