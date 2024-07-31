#Import necessary modules
from datetime import datetime
from operations import *
from read import *
from write import *


# display first heading of welcome message to user
print("\n\n\n")
print("\t\t\t\t\t\t\t\t!!!!!!!LAPTOP INDUSTRIES !!!!!!!")
print("\n")

    
stored_in_dictionary()
laptop_data =stored_in_dictionary() 
# display the available laptop stock    
display_stock()



#while loop for continuous functionality
loop = True
while loop == True:
    #ask user to enter correct option
    print("\n")
    print("Press 1 to sale laptop.")
    print("Press 2 to purchase laptop.")
    print("Press 3 to Exit.")
    print("\n")
    #check user input for validity
    loop_check = True
    while loop_check == True:
        try:
            user_input = int(input("Enter the option to continue: "))
            loop_check = False
        except:
            print("Please enter a valid detail!")
    print("\n")
    
    if user_input==1:     
        print("To generate a bill, provide the details: ")
        print("\n")
        name = input("Enter name of the customer: ")
        print("\n")
        phone = input("Enter the phone number: ")
        print("\n")

        user_purchased_laptops = []#[name,brand,price,quantity,total price],[name,brand,price,quantity,total price],
      

        loop_1 = True
        while loop_1 == True:
            display_stock()
            #validate id
            #also check if quantity is zero or not
            laptop_data =stored_in_dictionary() 
            user_id = validate_id(laptop_data)
            if int(laptop_data[user_id][3]) == 0:
                print("The product is currently out of stock!!!")
                loop_1 = True
            else:
                quantity_details = laptop_data[user_id][3]
                quantity = sales_quantity(quantity_details)
                print("\n")
                
                #update stock
                laptop_data[user_id][3] = int(laptop_data[user_id][3]) - int(quantity)
                updating_function(laptop_data)
                
                #pricing
                product_name = laptop_data[user_id][0]
                product_brand = laptop_data[user_id][1]
                selected_laptop_quantity = quantity
                unit_price = laptop_data[user_id][2]
                selected_item_price = laptop_data[user_id][2].replace("$",'')
                total_price = int(selected_item_price)*int(selected_laptop_quantity)
                user_purchased_laptops.append([product_name,product_brand, selected_laptop_quantity,unit_price,total_price])

                buy_more = input("do you want to continue y n").upper()
                if buy_more == "Y":
                    loop_1 = True
                else:
                    sales_receipt(user_purchased_laptops,name,phone)
                    loop_1 = False
    
    elif user_input==2:
        print("To generate a bill, provide the details: ")
        print("\n")
        name = input("Enter name of the manufacturer: ")
        print("\n")
        phone = input("Enter the phone number: ")
        print("\n")

        user_purchased_laptops = []
      

        loop_1 = True
        while loop_1 == True:
            display_stock()
            #validateid
            #also check if quantity is zero or not
            laptop_data =stored_in_dictionary() 
            user_id = validate_id(laptop_data)
      
            quantity_details = laptop_data[user_id][3]
            quantity = purchase_quantity(quantity_details)
            print("\n")
                
            #update stock
            laptop_data[user_id][3] = int(laptop_data[user_id][3]) + int(quantity)
            updating_function(laptop_data)
                
            #pricing
            product_name = laptop_data[user_id][0]
            product_brand = laptop_data[user_id][1]
            selected_laptop_quantity = quantity
            unit_price = laptop_data[user_id][2]
            selected_item_price = laptop_data[user_id][2].replace("$",'')
            total_price = int(selected_item_price)*int(selected_laptop_quantity)
            user_purchased_laptops.append([product_name,product_brand, selected_laptop_quantity,unit_price,total_price])

            buy_more = input("do you want to continue y n").upper()
            if buy_more == "Y":
                loop_1 = True
            else:
                purchase_receipt(user_purchased_laptops,name,phone)
                loop_1 = False
     

    elif user_input == 3:
        loop = False
        print("Thank you for your time with us!!!")
        print("\n")

    else:
        print("\n")
        print("Invalid choice")
        print("Options ID are: 1,2 and 3")
  
