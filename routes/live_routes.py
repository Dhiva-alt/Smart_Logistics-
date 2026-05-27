from flask import Blueprint,jsonify
import random

live_bp=Blueprint(
    "live",
    __name__
)

lat=13.0827
lon=80.2707

statuses=[

"On Route",
"Delayed",
"Traffic Alert",
"Delivered"

]


@live_bp.route(
"/live-location"
)

def live_location():

    global lat,lon

    lat += random.uniform(
        0.0002,
        0.0007
    )

    lon += random.uniform(
        0.0002,
        0.0007
    )

    return jsonify({

        "status":
        random.choice(
            statuses
        ),

        "lat":
        lat,

        "lon":
        lon

    })