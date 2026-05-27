from flask import Blueprint,request,jsonify
import pandas as pd
import os

chat_bp=Blueprint(
    "chat",
    __name__
)

df=pd.read_csv(
    "enhanced_delivery_data.csv"
)

@chat_bp.route(
    "/chat",
    methods=["POST"]
)
def chat():

    data=request.get_json()

    message=data.get(
        "message",
        ""
    ).lower().strip()


    if "delivery" in message:

        answer=f"""
Total deliveries:
{len(df)}
"""

    elif "average" in message and "time" in message:

        avg=round(
            df[
            "Delivery_Time_min"
            ].mean(),
            1
        )

        answer=f"""
Average delivery time:
{avg} minutes
"""

    elif "distance" in message:

        total=round(
            df[
            "Distance_km"
            ].sum(),
            1
        )

        answer=f"""
Total distance:
{total} km
"""

    elif "driver" in message:

        score=round(
            df[
            "Driver_Score"
            ].mean(),
            1
        )

        answer=f"""
Average driver score:
{score}
"""

    elif "vehicle" in message:

        vehicles = df[
            "Vehicle_Type"
        ].value_counts().to_dict()

        answer = str(
            vehicles
        )

    else:

        answer="""
I can help with:

• deliveries
• drivers
• weather
• distance
• vehicles
"""

    return jsonify({

        "response":
        answer

    })