import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    mean_absolute_error,
    r2_score,
    accuracy_score
)

# ======================================
# LOAD DATASET
# ======================================

df = pd.read_csv(
r"C:\Users\Divashini PC\Downloads\Food_Delivery_Times.csv"
)

print("Dataset Loaded Successfully")

# ======================================
# HANDLE MISSING VALUES
# ======================================

df = df.ffill()

# ======================================
# ENCODE CATEGORICAL DATA
# ======================================

encoder=LabelEncoder()

df['Weather']=encoder.fit_transform(df['Weather'])

df['Traffic_Level']=encoder.fit_transform(
df['Traffic_Level']
)

df['Time_of_Day']=encoder.fit_transform(
df['Time_of_Day']
)

df['Vehicle_Type']=encoder.fit_transform(
df['Vehicle_Type']
)

# ======================================
# LINEAR REGRESSION
# DELIVERY TIME PREDICTION
# ======================================

X=df[
[
'Distance_km',
'Weather',
'Traffic_Level',
'Time_of_Day',
'Vehicle_Type',
'Preparation_Time_min',
'Courier_Experience_yrs'
]
]

y=df['Delivery_Time_min']

X_train,X_test,y_train,y_test= train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

model=LinearRegression()

model.fit(
X_train,
y_train
)

predictions=model.predict(X_test)

mae=mean_absolute_error(
y_test,
predictions
)

r2=r2_score(
y_test,
predictions
)

print("\n========== REGRESSION ==========")

print("Model Trained Successfully")

print("Mean Absolute Error:",mae)

print("R2 Score:",r2)

# ======================================
# SAMPLE PREDICTION
# ======================================

sample=pd.DataFrame([[
10,
0,
1,
2,
1,
15,
3
]],columns=[
'Distance_km',
'Weather',
'Traffic_Level',
'Time_of_Day',
'Vehicle_Type',
'Preparation_Time_min',
'Courier_Experience_yrs'
])

result=model.predict(sample)

print(
"Predicted Delivery Time:",
round(result[0],2),
"minutes"
)

# ======================================
# CREATE DELIVERY STATUS
# ======================================

df['Delivery_Status']=df[
'Delivery_Time_min'
].apply(

lambda x:

'Delayed'
if x>60

else(
'On Time'
if x>=40
else 'Fast'
)

)

print("\nDelivery Status Created")

# ======================================
# CLASSIFICATION MODEL
# PREDICT DELIVERY STATUS
# ======================================

X2=df.drop(
[
'Delivery_Status',
'Delivery_Time_min'
],
axis=1
)

y2=df['Delivery_Status']

X_train2,X_test2,y_train2,y_test2= train_test_split(

X2,
y2,
test_size=0.2,
random_state=42

)

model2=RandomForestClassifier(
n_estimators=100,
random_state=42
)

model2.fit(
X_train2,
y_train2
)

pred2=model2.predict(
X_test2
)

accuracy=accuracy_score(
y_test2,
pred2
)

print("\n========== CLASSIFICATION ==========")

print(
"Delivery Status Accuracy:",
round(
accuracy*100,
2
),
"%"
)

# ======================================
# EXPORT ACTUAL VS PREDICTED
# ======================================

results=pd.DataFrame({

'Actual':y_test.values,

'Predicted':predictions

})

results.to_csv(

r"E:\prediction_results.csv",

index=False

)

print(
"\nprediction_results.csv saved"
)

# ======================================
# EXPORT STATUS PREDICTION
# ======================================

status_results=pd.DataFrame({

'Actual_Status':y_test2.values,

'Predicted_Status':pred2

})

status_results.to_csv(

r"E:\delivery_status_prediction.csv",

index=False

)

print(
"delivery_status_prediction.csv saved"
)

print(
"\nAll tasks completed successfully"
)
# ======================================
# DRIVER PERFORMANCE SCORE
# ======================================

df['Driver_Score']=(

(10-df['Delivery_Time_min']/10)

+

(df['Courier_Experience_yrs'])

)

print(
"\nDriver Score Created"
)

print(
df[
['Courier_Experience_yrs',
'Delivery_Time_min',
'Driver_Score']
].head()
)
# ======================================
# DELAY ALERT
# ======================================

df['Delay_Alert']=df[
'Delivery_Time_min'
].apply(

lambda x:
'ALERT'
if x>70
else 'Normal'

)

print(
"\nDelay Alert Added"
)

print(
df[
['Delivery_Time_min',
'Delay_Alert']
].head()
)
# ======================================
# SMART RECOMMENDATION
# ======================================

def recommendation(row):

    if row['Traffic_Level']==0:

        return "Use Bike"

    elif row['Weather']==3:

        return "Avoid Scooter"

    else:

        return "Standard Route"

df['Recommendation']=df.apply(
recommendation,
axis=1
)

print(
"\nRecommendation System Added"
)

print(
df[
['Traffic_Level',
'Weather',
'Recommendation']
].head()
)
df.to_csv(
r"E:\enhanced_delivery_data.csv",
index=False
)

print(
"\nEnhanced Dataset Saved"
)
# ======================================
# ROUTE OPTIMIZATION SCORE
# ======================================

df['Route_Score']=(

100

-

(df['Distance_km']*2)

-

(df['Delivery_Time_min']/2)

)

print(
"\nRoute Optimization Score Added"
)

print(
df[
[
'Distance_km',
'Delivery_Time_min',
'Route_Score'
]
].head()
)
# ======================================
# FUEL EFFICIENCY
# ======================================

df['Fuel_Efficiency']= (

50

/

df['Distance_km']

)

print(
"\nFuel Efficiency Added"
)

print(
df[
[
'Distance_km',
'Fuel_Efficiency'
]
].head()
)
# ======================================
# WAREHOUSE UTILIZATION
# ======================================

df['Warehouse_Utilization']= (

df['Preparation_Time_min']

*2

)

print(
"\nWarehouse Utilization Added"
)
df.to_csv(

r"E:\final_enhanced_delivery_data.csv",

index=False

)

print(
"\nFinal Dataset Saved"
)
months=[
"Jan","Feb","Mar","Apr",
"May","Jun","Jul","Aug",
"Sep","Oct","Nov","Dec"
]

df['Month']= np.random.choice(
months,
size=len(df)
)

monthly=df.groupby(
'Month'
).size().reset_index()

monthly.columns=[
'Month',
'Shipment_Count'
]

monthly.to_csv(
r"E:\monthly_trends.csv",
index=False
)

print(
"\nMonthly Trend File Saved"
)
delay_data=df.groupby(

['Traffic_Level','Weather']

)[

'Delivery_Time_min'

].mean().reset_index()

delay_data.to_csv(

r"E:\delay_heatmap.csv",

index=False

)

print(
"\nHeatmap Dataset Saved"
)
poor_routes=df[

df['Route_Score']<50

]

poor_routes.to_csv(

r"E:\poor_routes.csv",

index=False

)

print(
"\nPoor Routes Saved"
)
poor_routes=df[

df['Route_Score']<50

]

poor_routes.to_csv(

r"E:\poor_routes.csv",

index=False

)

print(
"\nPoor Routes Saved"
)
# ======================================
# SLA MONITORING
# ======================================

df['SLA_Status'] = df[
'Delivery_Time_min'
].apply(

lambda x:

'SLA Met'

if x<=60

else 'SLA Violated'

)

print(
"\nSLA Monitoring Added"
)

print(
df[
[
'Delivery_Time_min',
'SLA_Status'
]
].head()
)

df.to_csv(
r"E:\sla_delivery_data.csv",
index=False
)

print(
"SLA dataset saved"
)