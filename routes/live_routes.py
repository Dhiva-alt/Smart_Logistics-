from flask import Blueprint
from flask_socketio import emit
import threading
import time
import random

live_bp=Blueprint(
    'live',
    __name__
)

statuses=[

"On Route",
"Delayed",
"Delivered",
"Traffic Alert"

]

def send_updates(socketio):

    while True:

        data={

        "status":
        random.choice(statuses)

        }

        socketio.emit(
        "driver_update",
        data
        )

        time.sleep(8)


def start_live(socketio):

    thread=threading.Thread(

    target=send_updates,

    args=(socketio,)

    )

    thread.daemon=True

    thread.start()