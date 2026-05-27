USE smart_logistics_db;

SELECT * FROM delivery_data;
SELECT Delivery_Status, COUNT(*) AS Total
FROM delivery_data
GROUP BY Delivery_Status;

SELECT COUNT(*) AS Total_Orders
FROM delivery_data;

SELECT COUNT(*) AS Delayed_Orders
FROM delivery_data
WHERE Delivery_Status = 'Delayed';

SELECT Delivery_Status,
COUNT(*) AS Total_Orders
FROM delivery_data
GROUP BY Delivery_Status;

SELECT AVG(Delivery_Time_min) AS Avg_Delivery_Time
FROM delivery_data;

SELECT Vehicle_Type,
AVG(Delivery_Time_min) AS Avg_Time
FROM delivery_data
GROUP BY Vehicle_Type
ORDER BY Avg_Time;

SELECT Traffic_Level,
AVG(Delivery_Time_min) AS Avg_Delay
FROM delivery_data
GROUP BY Traffic_Level
ORDER BY Avg_Delay DESC;

SELECT Weather,
AVG(Delivery_Time_min) AS Avg_Time
FROM delivery_data
GROUP BY Weather
ORDER BY Avg_Time DESC;

SELECT Time_of_Day,
AVG(Delivery_Time_min) AS Avg_Time
FROM delivery_data
GROUP BY Time_of_Day;

SELECT *
FROM delivery_data
WHERE Distance_km > 15;

SELECT *
FROM delivery_data
ORDER BY Courier_Experience_yrs DESC
LIMIT 10;

SELECT Traffic_Level,
COUNT(*) AS Delayed_Orders
FROM delivery_data
WHERE Delivery_Status='Delayed'
GROUP BY Traffic_Level;

SELECT Weather,
COUNT(*) AS Delayed_Orders
FROM delivery_data
WHERE Delivery_Status='Delayed'
GROUP BY Weather;

SELECT Vehicle_Type,
AVG(Distance_km) AS Avg_Distance
FROM delivery_data
GROUP BY Vehicle_Type;

SELECT
COUNT(*) AS Total_Orders,
AVG(Delivery_Time_min) AS Avg_Delivery_Time,
AVG(Distance_km) AS Avg_Distance,
AVG(Courier_Experience_yrs) AS Avg_Experience
FROM delivery_data;

SELECT Weather,
Traffic_Level,
AVG(Delivery_Time_min) AS Avg_Time
FROM delivery_data
GROUP BY Weather, Traffic_Level
ORDER BY Avg_Time DESC;