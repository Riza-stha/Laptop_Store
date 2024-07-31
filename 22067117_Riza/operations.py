# Function to validate the user-provided laptop ID
def validate_id(laptop_data):
    loop = True
    while loop == True:
        try:
            print("\n")
            user_id = int(input("Please provide id of the laptop: "))# User input for laptop ID
            print("\n")
            loop = False
        except:
            print("Please enter a valid detail.")
    while user_id <=0 or user_id > len(laptop_data):
        print("\n")
        print("Invalid choice! Product ID are: 1,2,3,4 and 5")
        loop = True
        while loop == True:
            try:
                print("\n")
                user_id = int(input("Please provide id  of laptop: "))
                print("\n")
                loop = False
            except:
                print("Please enter a valid detail.")  
    return user_id # Returns the validated laptop ID

# Function to validate the quantity of laptops to be sold   
def sales_quantity(quantity_details):
    loop = True
    while loop == True:
        try:
            print("\n")
            quantity = int(input("Please provide quantity  of laptop you want to sell: "))
            print("\n")
            loop = False
        except:
            print("Please enter a valid detail.")
    while quantity <=0 or quantity > int(quantity_details):
        print("\n")
        print("Invalid choice! ")
        loop = True
        while loop == True:
            try:
                print("\n")
                quantity = int(input("Please provide quantity  of laptop you want to sell: "))
                print("\n")
                loop = False
            except:
                print("Please enter a valid detail.")  
    return quantity

# Function to validate the quantity of laptops to be purchased
def purchase_quantity(quantity_details):
    loop = True
    while loop == True:
        try:
            print("\n")
            quantity = int(input("Please provide quantity  of laptop you want to purchase: "))
            print("\n")
            loop = False
        except:
            print("Please enter a valid detail.")
    while quantity <=0:
        print("\n")
        print("Invalid choice!")
        loop = True
        while loop == True:
            try:
                print("\n")
                quantity = int(input("Please provide quantity  of laptop you want to purchase: "))
                print("\n")
                loop = False
            except:
                print("Please enter a valid detail.")  
    return quantity

