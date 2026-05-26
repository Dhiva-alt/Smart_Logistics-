from flask_mail import Message
from config.mail_config import mail


def send_alert():

    msg=Message(
        "Smart Logistics Alert",
        sender="yourgmail@gmail.com",
        recipients=["yourgmail@gmail.com"]
    )

    msg.body="""
Delivery Delay Alert

A shipment delay has been detected.
Check dashboard immediately.
"""

    mail.send(msg)

    print("Email Sent")