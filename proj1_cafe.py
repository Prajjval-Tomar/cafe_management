# 1st mini project (cafe management)
# Define the menu of Restaurant
menu = { 'Pizza':150,
         'Pasta':80,
         'Burger':130,
         'Soup':70,
         'Tea':20,
         'Coffee':25,
         'Milk':30
    }
#Great
print("\nWelcome to our Star Restaurant. Here's The Menu")
#print menu
print("\nPizza:        Rs150\nPasta:        Rs80\nBurger:       Rs130\nSoup:         Rs70\nTea:          Rs20\nCoffee:       Rs25\nMilk:         Rs30")
       
Total_Order = 0 #80+70=150 stored in total order
order_1 = input('Enter the name of item you want to order = ')

# Condition using membership operator
if order_1 in menu:
    Total_Order += menu[order_1] #0+50=50
    print(f'\n Your item {order_1} has been added to your order')
else:
    print(f'Your item {order_1} is not available yet!\n')
    
#user input for add another order
Another_Order = input('\n Do you want to add another item? (Yes/No)= ')
if Another_Order == 'Yes':
    order_2 = input('\n Enter the name of second item = ')
    if  order_2 in menu:
        Total_Order += menu[order_2]
        print(f'\n Your item {order_2} has been added to your order')
    else:
        print(f'\n Your item {order_2} is not available!')
        
print(f' \nThe total amount of orders to pay RS{Total_Order}')
    
        
        
    
    
    
    
             
       
       
       
