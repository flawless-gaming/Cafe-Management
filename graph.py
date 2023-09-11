from matplotlib import pyplot as plt
import sqlite3 as sql
import pandas as pd

def product_sales(): # Product-wise sales analysis
    con=sql.connect('flawless_cafe_data.db')
    c=con.cursor()
    c.execute('''SELECT Name,SUM(qty) FROM daily_orders WHERE Name!='Discount' AND Name!='TOTAL' AND
                Name!='Payable Amount' GROUP BY Name''')
    # ^ To execute the entered command in MySQL
    D=c.fetchall()
    df=pd.DataFrame(D,columns=['Name','Qty']) # To create DataFrame from the fetched data
    print(df)
    plt.rcParams.update({'font.size':7}) # To change the font size
    gr=plt.barh(df.Name,df.Qty) # To create a horizontal bar graph
    plt.xlabel('Product')
    plt.ylabel('Quantity')
    plt.title('Food Sales Analysis')
    plt.show()
    
def daily_sales():
    con=sql.connect('flawless_cafe_data.db')
    c=con.cursor()
    c.execute("SELECT Date,SUM(Price) AS 'Sales Amount' FROM daily_orders WHERE Name = 'TOTAL' GROUP BY Date")
    # ^ To fetch data on the basis of date
    D=c.fetchall()
    df=pd.DataFrame(D,columns=['DATE','AMOUNT']) # To create DataFrame from the fetched data
    print(df)
    gr=plt.bar(df.DATE,df.AMOUNT) # To create a bar graph
    plt.xlabel('Date')
    plt.ylabel('Volume of Sales')
    plt.title('Food Sales Analysis')
    plt.show()