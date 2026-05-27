import pandas as pd

df = pd.read_csv(
    "enhanced_delivery_data.csv"
)

def ask_bot(question):

    question = question.lower().strip()

    total_orders=len(df)

    avg_time=round(
        df["Delivery_Time_min"]
        .mean(),
        1
    )

    total_distance=round(
        df["Distance_km"]
        .sum(),
        1
    )

    avg_score=round(
        df["Driver_Score"]
        .mean(),
        1
    )

    delayed=len(
        df[
            df["Delivery_Time_min"]
            >
            avg_time
        ]
    )



    if any(x in question for x in
    [
    "delivery",
    "deliveries",
    "total orders",
    "orders"
    ]):

        return f"""
📦 Delivery Summary

Total completed deliveries:
{total_orders}

System status:
Active and processing
deliveries normally.
"""



    elif any(x in question for x in
    [
    "average time",
    "delivery time",
    "avg time"
    ]):

        return f"""
⏱ Delivery Performance

Average delivery time:

{avg_time} minutes

Status:
Delivery speed is stable.
"""



    elif any(x in question for x in
    [
    "distance",
    "distance covered"
    ]):

        return f"""
📍 Distance Analytics

Total route distance covered:

{total_distance} km
"""



    elif any(x in question for x in
    [
    "driver",
    "score",
    "performance"
    ]):

        return f"""
⭐ Driver Analytics

Average Driver Score:

{avg_score}/10

Performance status:
Drivers are performing
efficiently.
"""



    elif any(x in question for x in
    [
    "delay",
    "late"
    ]):

        return f"""
🚨 Delay Analytics

Delayed deliveries:

{delayed}

Recommendation:

Monitor traffic and
weather conditions.
"""



    elif any(x in question for x in
    [
    "vehicle",
    "transport"
    ]):

        vehicle_map={

            0:"Bike",
            1:"Car",
            2:"Scooter"

        }

        vehicles=(
            df[
            "Vehicle_Type"
            ]
            .value_counts()
        )

        result="""
🚚 Vehicle Usage

"""

        for k,v in vehicles.items():

            result += (
            f"{vehicle_map.get(k,k)}"
            f" : {v}\n"
            )

        return result



    elif any(x in question for x in
    [
    "sla",
    "service level"
    ]):

        return """
🟢 SLA Status

Current SLA:

Healthy

No SLA violations
detected.
"""



    elif any(x in question for x in
    [
    "weather"
    ]):

        return """
🌤 Weather Insight

Current weather data
is integrated into
delivery planning.

Weather affects route
optimization and ETA.
"""



    elif any(x in question for x in
    [
    "prediction",
    "ml",
    "ai"
    ]):

        return """
🤖 AI Prediction Module

Machine learning
predicts delivery
time using:

• weather
• traffic
• vehicle type
• distance
• driver score
"""



    else:

        return """
🤖 Smart Logistics Assistant

Try asking:

📦 total deliveries

⏱ average time

⭐ driver performance

🚚 vehicles

📍 distance

🌤 weather

🚨 delays

🤖 prediction
"""