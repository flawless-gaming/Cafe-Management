import pandas as pd,numpy as np,random
import connector
import time
from datetime import date

def bill():
    order=pd.read_csv('order.csv')
    total=order.iat[-1,-1] # To create a dataframe consisting ordered items and their price
    o=input('~ Press 1 to get a discount on your order(upto 45%)> ') # To give discount on the order
    if o=='1':
        #z=int(np.random.randint(0,45,1)) # random value is generated using numpy
        z=34
        print('~ Got ',z,'% off!','\n',sep='')
        # If anything other than '1' is entered, discount won't be applied
    else:
        z=0
    a=len(order.Name)
    c=random.randint(1000,9999)
    dt=date.today()
    tm=time.strftime('%H:%M:%S')
    order.loc[:,'Date']=dt
    print('-----------Bill Number:',c,'----------',sep='')
    print('-----------Date:',dt,'-----------',sep='')
    print('------------Time:',tm,'------------',sep='')
    off=total*z/100
    order.insert(loc=0, column='Order_no', value=c)
    order.loc[a]=c,'Discount',' ',off,dt # To add a new row 'Offer'
    a=len(order.index)
    order.loc[a]=c,'Payable Amount',' ',total-off,dt
    print(order.drop(['Order_no','Date'],axis=1))
    order=order.to_csv('bill.csv',index=False)
    connector.save()
    print('~ Thank You for visiting Flawless Coffee! We hope to see you again.')
    