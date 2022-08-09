-- Displays the average temperature (in Fahrenheit)
-- by city ordered by descending temperature.
SELCT city, AVG(value) AS avg_temp
FROM tempratures
GROUP BY city
ORDER BY avg_temp DESC
