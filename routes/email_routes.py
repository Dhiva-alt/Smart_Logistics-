from flask import Blueprint
from services.email_service import send_alert

email_bp=Blueprint(
'email',
__name__
)

@email_bp.route('/send-alert')

def alert():

    send_alert()

    return {

    "message":
    "Alert Email Sent"

    }