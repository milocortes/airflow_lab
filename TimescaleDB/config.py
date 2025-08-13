
import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password="password",
    port = "5424"
)

cur = conn.cursor()

cur.execute(
"""
CREATE TABLE IF NOT EXISTS stock_prices(
    time TIMESTAMPTZ,
    ticker TEXT,
    price DOUBLE PRECISION
)
"""
)

cur.execute("SELECT create_hypertable('stock_prices', 'time')")

conn.commit()

import random
import datetime
from datetime import datetime, timedelta, timezone
from pytz import timezone

for i in range(10_000):
    random_date = datetime.now(timezone.utc) - timedelta(days=random.randint(0, 365))
    cur.execute("INSERT INTO stock_prices (time, ticker, price) VALUES (%s, %s, %s)", (random_date, "APL", random.uniform(100,200)))


conn.commit()

cur.execute(

"""
SELECT
  time_bucket('3 month', time) AS bucket,
  AVG(price) AS avg_temp
FROM
  stock_prices
GROUP BY
  bucket
ORDER BY
  bucket ASC;
"""
)

results = cur.fetchall()

results