-- displays top 3 cities with highest average temperature in July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month=7 or MONTH=8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
