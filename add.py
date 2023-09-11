import pandas as pd
import numpy as np
data={}
Qty=[]
'''
# General syntax for adding an item to a customer's order.
--> if Category==Choice:
        a=int(input('> Quantity> '))
        print('~ Added ',a,'x Item to your order',sep='')
        x='Item'
        data[x]=a*Price
        Qty.append(a)
'''
def Coffee(): # To create a menu for Coffee beverages
    while True:
        print('  +----------------------------------+')
        print('~ |              Coffee              |')
        print('  +----------------------------------+')
        print('  | 1.Latte                    99/-  |')
        print('  | 2.Mocha                    99/-  |')
        print('  | 3.Caramel Macchiato       199/-  |')
        print('  | 4.White Chocolate Mocha   179/-  |')
        print('  | 5.Americano               119/-  |')
        print('  | 6.Cold Coffee              79/-  |')
        print('  | 7.Flat White              149/-  |')
        print('  |                ← Back to Menu(0) |')
        print('  +----------------------------------+')
        Coffee=int(input('> Enter Your Choice> '))
        
        if Coffee==1:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Latte to your order',sep='')
            c1='Latte'
            data[c1]=a*99
            Qty.append(a)
            
        elif Coffee==2:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Mocha to your order',sep='')
            c2='Mocha'
            data[c2]=a*99
            Qty.append(a)
            
        elif Coffee==3:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Caramel Macchiato to your order',sep='')
            c3='Caramel Macchiato'
            data[c3]=a*199
            Qty.append(a)
                
        elif Coffee==4:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x White Chocolate Mocha to your order',sep='')
            c4='White Chocolate Mocha'
            data[c4]=a*179
            Qty.append(a)
                
        elif Coffee==5:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Americano to your order',sep='')
            c5='Americano'
            data[c5]=a*119
            Qty.append(a)
        
        elif Coffee==6:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Cold Coffee to your order',sep='')
            c6='Cold Coffee'
            data[c6]=a*79
            Qty.append(a)
        
        elif Coffee==7:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Flat White to your order',sep='')
            c7='Flat White'
            data[c7]=a*149
            Qty.append(a)

        elif Coffee==0:
            print()
            break

        else:
            print('!~Please enter a valid number.')

def Tea(): # To create a menu for Tea beverages
    while True:
        print('  +----------------------------------+')
        print('~ |               Tea                |')
        print('  +----------------------------------+')
        print('  | 1.Hot Tea                  49/-  |')
        print('  | 2.Iced Tea                 59/-  |')
        print('  | 3.Jasmine Tea              79/-  |')
        print('  | 4.Green Tea                59/-  |')
        print('  | 5.Black Tea                49/-  |')
        print('  |                ← Back to Menu(0) |')
        print('  +----------------------------------+')
        Tea=int(input('> Enter Your Choice> '))
            
        if Tea==1:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Hot Tea to your order',sep='')
            t1='Hot Tea'
            data[t1]=a*49
            Qty.append(a)
                
        elif Tea==2:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Iced Tea to your order',sep='')
            t2='Iced Tea'
            data[t2]=a*59
            Qty.append(a)
                
        elif Tea==3:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Jasmine Tea to your order',sep='')
            t3='Jasmine Tea'
            data[t3]=a*79
            Qty.append(a)
                
        elif Tea==4:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Green Tea to your order',sep='')
            t4='Green Tea'
            data[t4]=a*59
            Qty.append(a)
                
        elif Tea==5:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Black Tea to your order',sep='')
            t5='Black Tea'
            data[t5]=a*49
            Qty.append(a)
                
        elif Tea==0:
            print()
            break
        
        else:
            print('!~Please enter a valid number.')

def Frappe(): # To create a menu for Frappe beverages
    while True:
        print('  +----------------------------------+')
        print('~ |              Frappe              |')
        print('  +----------------------------------+')
        print('  | 1.Double Chocolate        149/-  |')
        print('  | 2.Mocha                   179/-  |')
        print('  | 3.Caramel                 179/-  |')
        print('  | 4.Mango Caramel           199/-  |')
        print('  | 5.Strawberry Oreo         249/-  |')
        print('  |                ← Back to Menu(0) |')
        print('  +----------------------------------+')
        Frappe=int(input('> Enter Your Choice> '))
        
        if Frappe==1:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Double Chocolate Frappe to your order',sep='')
            f1='Double Chocolate Frappe'
            data[f1]=a*149
            Qty.append(a)
        
        elif Frappe==2:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Mocha Frappe to your order',sep='')
            f2='Mocha Frappe'
            data[f2]=a*179
            Qty.append(a)
            
        elif Frappe==3:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Caramel Frappe to your order',sep='')
            f3='Caramel Frappe'
            data[f3]=a*179
            Qty.append(a)
            
        elif Frappe==4:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Mango Caramel Frappe to your order',sep='')
            f4='Mango Caramel Frappe'
            data[f4]=a*199
            Qty.append(a)
        
        elif Frappe==5:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Strawberry Oreo to your order',sep='')
            f5='Strawberry Oreo'
            data[f5]=a*249
            Qty.append(a)
        
        elif Frappe==0:
            print()
            break
        
        else:
            print('!~Please enter a valid number.')

def Fast_Food(): # To create a menu for Fast Food
    while True:
        print('  +----------------------------------+')
        print('~ |             Fast Food            |')
        print('  +----------------------------------+')
        print('  | 1.Hashbrown                29/-  |')
        print('  | 2.Aloo Tikki Burger        79/-  |')
        print('  | 3.Spicy Chicken Burger    199/-  |')
        print('  | 4.Paneer Taco              99/-  |')
        print('  | 5.Chicken Taco            149/-  |')
        print('  | 6.Fish and Chips          199/-  |')
        print('  | 7.Salted Fries             79/-  |')
        print('  |                ← Back to Menu(0) |')
        print('  +----------------------------------+')
        Fast_Food=int(input('> Enter Your Choice> '))
        
        if Fast_Food==1:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Hashbrown to your order',sep='')
            ff1='Hashbrown'
            data[ff1]=a*29
            Qty.append(a)
        
        elif Fast_Food==2:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Aloo Tikki Burger to your order',sep='')
            ff2='Aloo Tikki Burger'
            data[ff2]=a*79
            Qty.append(a)
        
        elif Fast_Food==3:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Spicy Chicken Burger to your order',sep='')
            ff3='Spicy Chicken Burger'
            data[ff3]=a*199
            Qty.append(a)
            
        elif Fast_Food==4:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Paneer Taco to your order',sep='')
            ff4='Paneer Taco'
            data[ff4]=a*99
            Qty.append(a)
        
        elif Fast_Food==5:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Chicken Taco to your order',sep='')
            ff5='Chicken Taco'
            data[ff5]=a*149
            Qty.append(a)
        
        elif Fast_Food==6:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Fish and Chips to your order',sep='')
            ff6='Fish and Chips'
            data[ff6]=a*199
            Qty.append(a)
        
        elif Fast_Food==7:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Salted Fries to your order',sep='')
            ff7='Salted Fries'
            data[ff7]=a*79
            Qty.append(a)
        
        elif Fast_Food==0:
            print()
            break
        
        else:
            print('!~Please enter a valid number.')

def Desserts(): # To create a menu for Desserts
    while True:
        print('  +----------------------------------+')
        print('~ |             Desserts             |')
        print('  +----------------------------------+')
        print('  | 1. Apple Pie               99/-  |')
        print('  | 2. Strwberry CheeseCake   179/-  |')
        print('  | 3. Chocolate Donut         49/-  |')
        print('  | 4. Red Velvet CupCake     119/-  |')
        print('  | 5. Mango Pudding           89/-  |')
        print('  | 6. Chocolate Brownie      159/-  |')
        print('  | 7. Chocolate Cookie        59/-  |')
        print('  |                ← Back to Menu(0) |')
        print('  +----------------------------------+')
        Desserts=int(input('> Enter Your Choice> '))
        
        if Desserts==1:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Apple Pie to your order',sep='')
            d1='Apple Pie'
            data[d1]=a*99
            Qty.append(a)
            
        elif Desserts==2:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Strwberry CheeseCake to your order',sep='')
            d2='Strwberry CheeseCake'
            data[d2]=a*179
            Qty.append(a)
            
        elif Desserts==3:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Chocolate Donut to your order',sep='')
            d3='Chocolate Donut'
            data[d3]=a*49
            Qty.append(a)
            
        elif Desserts==4:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Red Velvet CupCake to your order',sep='')
            d4='Red Velvet CupCake'
            data[d4]=a*119
            Qty.append(a)
            
        elif Desserts==5:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Mango Pudding to your order',sep='')
            d5='Mango Pudding'
            data[d5]=a*89
            Qty.append(a)
            
        elif Desserts==6:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Chocolate Brownie to your order',sep='')
            d6='Chocolate Brownie'
            data[d6]=a*159
            Qty.append(a)
        
        elif Desserts==7:
            a=int(input('> Quantity> '))
            print('~ Added ',a,'x Chocolate Cookie to your order',sep='')
            d='Chocolate Cookie'
            data[d7]=a*59
            Qty.append(a)
            
        elif Desserts==0:
            print()
            break
        
        else:
            print('!~Please enter a valid number.')
        
def Bill():
    keys,values=zip(*data.items()) # To seperate keys and values of a dictionary into a list
    a=(len(keys))
    total=sum(values)
    df=pd.DataFrame({'Name':keys,'Qty':Qty,'Price':values})
    df.at[a]='TOTAL',' ',total
    df=df.to_csv('order.csv',index=False)