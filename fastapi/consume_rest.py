# import requests module
import requests
import psycopg2
from datetime import datetime, timedelta, timezone

# Define connection
conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password="password",
    port = "5424"
)

# Making a get request
response = requests.get('http://127.0.0.1:8000')

# print json content
json_val = response.json() 
print(json_val)

valor = json_val["valor"]

# 
random_date = datetime.now(timezone.utc)

cur.execute("INSERT INTO stock_prices (time, ticker, price) VALUES (%s, %s, %s)", (random_date, "APL", valor))
conn.commit()

"""
SELECT
  time_bucket('5 minute', time) AS bucket,
  AVG(price) AS avg_temp
FROM
  stock_prices_fastapi
GROUP BY
  bucket
ORDER BY
  bucket ASC;
"""

