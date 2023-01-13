import pandas as pd
#function orders is created
def orders():
    print(' +----------------------------------+')
    print(' |            Your Order            |')
    print(' +----------------------------------+')
    df=pd.read_csv('order.csv')
    print(df)
