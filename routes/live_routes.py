from flask import Blueprint,jsonify
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


lat=13.0827
lon=80.2707


def send_updates(socketio):

    global lat,lon

    while True:

        lat += random.uniform(
        0.0001,
        0.0006
        )

        lon += random.uniform(
        0.0001,
        0.0006
        )


        data={

        "status":
        random.choice(statuses),

        "lat":
        lat,

        "lon":
        lon

        }


        socketio.emit(

        "driver_update",

        data

        )

        time.sleep(5)



def start_live(socketio):

    thread=threading.Thread(

    target=send_updates,

    args=(socketio,)

    )

    thread.daemon=True

    thread.start()