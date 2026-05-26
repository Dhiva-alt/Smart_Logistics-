import pandas as pd

df = pd.read_csv(
    "enhanced_delivery_data.csv"
)


def ask_bot(question):

    question = question.lower()


    if ("vehicle" in question or
        "best" in question or
        "perform" in question):

        result = df.groupby(
            "Vehicle_Type"
        )["Delivery_Time_min"].mean()

        best = result.idxmin()

        value = round(
            result.min(),
            2
        )

        return f"{best} performs best with average delivery time {value} minutes."


    elif ("delay" in question or
          "late" in question):

        avg = round(
            df["Delivery_Time_min"].mean(),
            2
        )

        return f"Average delivery time is {avg} mins. Weather and traffic are major causes of delays."


    elif ("driver" in question or
          "courier" in question):

        score = round(
            df["Driver_Score"].mean(),
            2
        )

        return f"Average driver score is {score}"


    elif ("route" in question):

        route = round(
            df["Route_Score"].mean(),
            2
        )

        return f"Route optimization score is {route}"


    elif ("fuel" in question):

        fuel = round(
            df["Fuel_Efficiency"].mean(),
            2
        )

        return f"Average fuel efficiency is {fuel}"


    else:

        return """
Ask:
- Which vehicle performs best?
- Why are deliveries delayed?
- Driver performance
- Route optimization
- Fuel efficiency
"""    