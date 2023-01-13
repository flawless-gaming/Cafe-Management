import sqlite3
import pandas as pd

def save():
    con=sqlite3.connect('flawless_cafe_data.db')
    c=con.cursor()
    users=pd.read_csv('bill.csv')
    users.to_sql('daily_orders',con,if_exists='append',index=False)
def verify():
    con=sqlite3.connect('flawless_cafe_data.db')
    c=con.cursor()
    c.execute("SELECT * FROM daily_orders")
    D=c.fetchall()
    df=pd.DataFrame(D,columns=['Id_no','Name','QTY','Price','Date'])
    no=int(input('Enter ID_NO :'))
    a=df.loc[df.Id_no==no]
    print(a)
def show():
    con=sqlite3.connect('flawless_cafe_data.db')
    c=con.cursor()
    c.execute("SELECT * FROM daily_orders")
    D=c.fetchall()
    df=pd.DataFrame(D,columns=['Id_no','Name','QTY','Price','Date'])
    print(df)