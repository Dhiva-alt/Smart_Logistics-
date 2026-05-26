from flask import Blueprint, render_template
import pandas as pd
from datetime import datetime
import requests
from services.sla_service import check_sla

mobile_bp=Blueprint(
    'mobile',
    __name__
)

df=pd.read_csv(
    r"E:\enhanced_delivery_data.csv"
)


# WEATHER API

API_KEY="ec6f3a50fe2e3c1073903a460fb777b2"

city="Chennai"

temp=0
condition="Unknown"

try:

    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response=requests.get(url)

    data=response.json()

    if "main" in data:

        temp=round(
            data['main']['temp'],
            1
        )

        condition=(
            data['weather'][0]
            ['description']
        )

except:

    pass



@mobile_bp.route('/driver')

def driver():

    total_orders=len(df)
    sla=check_sla()

    avg_delivery=round(
        df['Delivery_Time_min']
        .mean(),
        1
    )

    total_distance=round(
        df['Distance_km']
        .sum(),
        1
    )

    avg_score=round(
        df['Driver_Score']
        .mean(),
        1
    )

    prediction=round(

        df[
        'Delivery_Time_min'
        ]

        .sample(1)

        .iloc[0]

    )


    progress=min(

        round(
            prediction/
            avg_delivery*100
        ),

        100

    )


    top_vehicles=(

        df.groupby(
            'Vehicle_Type'
        )

        .agg({

            'Delivery_Time_min':
            'count',

            'Driver_Score':
            'mean'

        })

        .reset_index()

    )


    top_vehicles.columns=[

        'vehicle',
        'deliveries',
        'score'

    ]


    top_vehicles[
    'score'
    ]=top_vehicles[
    'score'
    ].round(1)


    top_vehicles=top_vehicles.to_dict(
        orient='records'
    )


    days=[

        "Sun",
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat"

    ]


    weekly_data=[

        120,
        210,
        260,
        300,
        350,
        420,
        280

    ]


    return render_template(

        "driver_dashboard.html",

        driver="John Driver",

        date=datetime.now().strftime(
        "%d %b %Y"
        ),

        deliveries=total_orders,

        avg_time=avg_delivery,

        distance=total_distance,

        score=avg_score,

        order=1023,

        prediction=prediction,

        status="On Route",

        progress=progress,

        alert=
        "Traffic detected near route",

        temp=temp,

        condition=
        condition.title(),

        start_lat=13.0827,

        start_lon=80.2707,

        end_lat=13.1143,

        end_lon=80.2830,

        days=days,

        weekly_data=weekly_data,

        top_vehicles=top_vehicles,
        sla=sla

    )