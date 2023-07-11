from multiprocessing import Value
from secrets import choice
from numpy import append
import calendar
from datetime import datetime
import openpyxl 
import os
  
# Give the location of the file 
path = r'C:\Users\pc\Documents\py pra\SHOP_M_S\Book.xlsx'
  
# To open the workbook 
# workbook object is created 
wb_obj = openpyxl.load_workbook(path) 
  
# Get workbook active sheet object 
# from the active attribute 
sheet1 = wb_obj.active 

sam = datetime.now()
current_time = sam.strftime("%H:%M:%S")

#stock = {
#    "Urea":"50 bags",
  #  "Dap":"60 Bags",
 #   "MOP":"80 Bags"
#}

stock = sheet1
with open('stock.txt', 'w') as f:
    f.write(str(stock))

def view_stock():
    for cell1, cell2 in sheet1:
          print(cell1.value, cell2.value)

def add_stock():
        new_stock=(input("Enter new product name "))
        new_stock_value=(input("Enter new product quantity "))
        stock[new_stock] = new_stock_value

def Sale():
     del_product=input("Enter the product that you want to remove from stock ")
     delate1 = stock.pop(del_product)
     print(f'Your prodcut {del_product} had removed ')



def new_bill(): 
    new_bill1=input("if you wanna to add new product enter 10.. ")
    if new_bill1=="9":
        billing()

def view_bills():
    for path in os.scandir(r'C:\Users\pc\Documents\py pra\SHOP_M_S\\bills'):
                 if path.is_file():
                    print(path.name)
    path_input=input('Enter the file name that you wanna open from above list...')
    #path1=(rf'C:\Users\pc\Documents\py pra\SHOP_M_S\\bills\\{path_input}', 'r')
    bill_open=open(rf'C:\Users\pc\Documents\py pra\SHOP_M_S\\bills\\{path_input}', 'r')
    print(bill_open.read())
    bill_open.close
    
def billing():
    shop_name = "JAI LAXMI TRADERS"
    namec=input("Enter customer names ")
    view_stock()
    print("Enter the product from above stock list ")
    buy_product=input("Enter product name ")
    buy_product_quantity=int(input("Enter product quantity "))
    price1=int(input(f'Enter the {buy_product} price. '))
    print_bill=f'''                  Dear {namec} thanks for purchasing from {shop_name}.....
                   PRODUCT NAME            QUANTITY                    RATE
                   {buy_product}           {buy_product_quantity}                                  {price1}


                   Time- {current_time}     
    
    '''
    if buy_product==stock['A2']:
        stock['B2'] - buy_product_quantity

    if buy_product==stock['A3']:
        stock['B3'] - buy_product_quantity

    if buy_product==stock['A4']:
        stock['B4'] - buy_product_quantity
    

    if buy_product==stock['A5']:
        stock['B5'] - buy_product_quantity

    if buy_product==stock['A6']:
        stock['B6'] - buy_product_quantity

    if buy_product==stock['A7']:
        stock['B7'] - buy_product_quantity

    if buy_product==stock['A8']:
        stock['B8'] - buy_product_quantity
    
    if buy_product==stock['A9']:
        stock['B9'] - buy_product_quantity

    if buy_product==stock['A10']:
        stock['B10'] - buy_product_quantity

    if buy_product==stock['A11']:
        stock['B11'] - buy_product_quantity
    #new_bill()

    

    #if buy_product_quantity<0:
       # stock[Value]-buy_product_quantity
          #append(stock)


    with open(f'bills/Bill of {namec}.txt', 'w') as f:
        f.write(print_bill)


    print(print_bill)





while (True):
    print('''
    Choose option
    1. for viwing stock
    2. for adding stock
    3. for delating products
    4. for billing
    5. for viewing bills
    ''')
    choice1 = input("Enter your choice ")
    if choice1=="1":
       view_stock()
    

    if choice1=="2":
       add_stock()
    

    if choice1=="3":
       Sale()
    
    if choice1=="4":
        billing()
        view_stock()

    if choice1=="5":
        view_bills()

    if choice1!="1"or"2"or"3"or"4":
        print("Select Valid option!")
