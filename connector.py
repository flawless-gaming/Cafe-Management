import sqlite3
import pandas as pd

def save(): # To create a function to add 'bill' to 'daily_orders'
    con=sqlite3.connect('flawless_cafe_data.db')
    c=con.cursor()
    users=pd.read_csv('bill.csv')
    users.to_sql('daily_orders',con,if_exists='append',index=False)

def verify(): # To verify the users data using order number
    con=sqlite3.connect('flawless_cafe_data.db')
    c=con.cursor()
    c.execute('SELECT * FROM daily_orders')
    D=c.fetchall()
    df=pd.DataFrame(D,columns=['Id_no','Name','Qty','Price','Date'])
    no=int(input('> Enter Id No.> '))
    a=df.loc[df.Id_no==no]
    print(a)

def show(): # Function to show the order history
    con=sqlite3.connect('flawless_cafe_data.db')
    c=con.cursor()
    c.execute('SELECT * FROM daily_orders')
    D=c.fetchall()
    df=pd.DataFrame(D,columns=['Id_no','Name','Qty','Price','Date'])
    print(df)