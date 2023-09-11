import add
import cancel
import exit
import orders
import staff
''' AIM : Placing an order, to be able to see the ordered items, to be able to cancel
         ordered items, to get a bill and to view the order history as staff.         '''
print('|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+|')
print('~ Welcome to Flawless Coffee')
mm=input('~ Press Enter to start ')
print('|-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+|')
def startmenu():
    print('  +----------------------------------+')
    print('~ |             Main Menu            |')
    print('  +----------------------------------+')
    print('  | 1.Place Order                    |')
    print('  | 2.Show Ordered Items             |')
    print('  | 3.Cancel Items                   |')
    print('  | 4.Print Bill                     |')
    print('  | 5.Staff Menu                     |')
    print('  +----------------------------------+')
    global inp
    inp=int(input('> Enter Your Choice> '))
startmenu()
while True:
    if inp==1: # Placing an order
        print('  +----------------------------------+')
        print('~ |            Order Menu            |')
        print('  +----------------------------------+')
        print('  | 1.Coffee                         |')
        print('  | 2.Tea                            |')
        print('  | 3.Frappe                         |')
        print('  | 4.Fast Food                      |')
        print('  | 5.Desserts                       |')
        print('  |           ← Back to Main Menu(0) |')
        print('  +----------------------------------+')
        x=input('> Enter Your Choice> ')
# Showing the Menu and asking for input ^
        
        if x=='1':
            add.Coffee()
            
        elif x=='2':
            add.Tea()
        
        elif x=='3':
            add.Frappe()
        
        elif x=='4':
            add.Fast_Food()
        
        elif x=='5':
            add.Desserts()
# To show the items of selected category ^
        
        elif x=='0': # '0' to return to the Main Menu
            startmenu()
            add.Bill()
            
    elif inp==2: # '2' to show ordered items
        orders.orders()
        mm=input('~ Press Enter to go to Main Menu ')
        startmenu()
        
    elif inp==3: # '3' to remove ordered items
        cancel.remove()
        mm=input('~ Press Enter to go to Main Menu ')
        startmenu()
   
    elif inp==4: # '4' to print the bill
        exit.bill()
        break
    
    elif inp==5: # '5' to access the staff menu
        staff.staff()
        startmenu()
        
    else: 
        print('!~ Please enter a valid number.')
        startmenu()