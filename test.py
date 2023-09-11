import pandas as pd
import sqlite3 as sql

con=sql.connect('flawless_cafe_data.db')
c=con.cursor()
c.execute("DROP TABLE daily_orders")
D=c.fetchall()
print(D)