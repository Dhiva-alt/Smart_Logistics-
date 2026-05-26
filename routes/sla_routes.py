from flask import Blueprint
from services.sla_service import check_sla

sla_bp = Blueprint(
    'sla',
    __name__
)

@sla_bp.route(
    '/sla'
)

def sla():

    result = check_sla()

    return result