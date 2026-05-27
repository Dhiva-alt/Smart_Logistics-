import pandas as pd

df = pd.read_csv(
    "enhanced_delivery_data.csv"
)


def ask_bot(question):

    question = question.lower().strip()

    if "delivery" in question:

        return f"""
Total deliveries:
{len(df)}
"""

    elif "average" in question and "time" in question:

        avg = round(
            df["Delivery_Time_min"]
            .mean(),
            1
        )

        return f"""
Average delivery time:
{avg} minutes
"""

    elif "distance" in question:

        total = round(
            df["Distance_km"]
            .sum(),
            1
        )

        return f"""
Total distance:
{total} km
"""

    elif "driver" in question:

        score = round(
            df["Driver_Score"]
            .mean(),
            1
        )

        return f"""
Average Driver Score:
{score}
"""

    elif "vehicle" in question:

        vehicles = (
            df["Vehicle_Type"]
            .value_counts()
            .to_dict()
        )

        return str(vehicles)

    else:

        return """
I can answer:

• deliveries
• average time
• driver score
• vehicles
• distance
"""