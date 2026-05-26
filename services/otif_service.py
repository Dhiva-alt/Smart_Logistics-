import pandas as pd

df=pd.read_csv(
"enhanced_delivery_data.csv"
)

def calculate_otif():

    df["OTIF"]=df["Delivery_Time_min"].apply(

        lambda x:
        "Success"
        if x<=60
        else "Failed"
    )

    total=len(df)

    success=len(
        df[
        df["OTIF"]=="Success"
        ]
    )

    percentage=round(
        success/total*100,
        2
    )

    return{

    "OTIF Percentage":
    f"{percentage}%",

    "Successful Deliveries":
    success,

    "Total Deliveries":
    total

    }