from flask import Blueprint
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
            0.0005
        )

        lon += random.uniform(
            0.0001,
            0.0005
        )

        data={

        "status":
        random.choice(statuses),

        "lat":
        lat,

        "lon":
        lon

        }

        print("sending:",data)

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