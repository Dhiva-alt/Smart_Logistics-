import pandas as pd

df = pd.read_csv(
    "enhanced_delivery_data.csv"
)


def check_sla():

    SLA_LIMIT = 60

    df["SLA_Status"] = df[
        "Delivery_Time_min"
    ].apply(

        lambda x:
        "On Time"
        if x <= SLA_LIMIT
        else "Violated"

    )


    total = len(df)

    ontime = len(
        df[
            df["SLA_Status"]=="On Time"
        ]
    )

    violated = len(
        df[
            df["SLA_Status"]=="Violated"
        ]
    )


    percent = round(
        (ontime/total)*100,
        2
    )


    return {

        "Total Deliveries":
        total,

        "On Time":
        ontime,

        "Violated":
        violated,

        "SLA Success Rate":
        f"{percent}%"
    }