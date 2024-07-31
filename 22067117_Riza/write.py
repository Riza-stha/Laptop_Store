#function to update data in the file
def updating_function(laptop_data):
    file = open("laptop_data.txt","w")
    for values in laptop_data.values():
        file.write(str(values[0]) + "," + str(values[1])+ ","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()

#function to generate the purchase receipt
def purchase_receipt(user_purchased_laptops,name,phone):
    total = 0
    VAT = 0.13

    # Calculate the total price of purchased laptops
    for i in user_purchased_laptops:
        total =total+ int(i[4])
    VAT_AMT = total * VAT
    grand_total = total +VAT_AMT

    # Print the purchase receipt                   
    print("\n")
    print("\t \t \t \t laptop shop bill")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9849408157")
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("laptop details are:")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Name of manufacturer:" + str(name))
    print("contact number:" + str(phone))
    #datetime
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Purchase Details are:")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Item Name \t\t Brand \t\t Total Quantity \t\t Unit Price \t\t\t Total")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    for i in user_purchased_laptops:
                
        print(i[0],"\t", i[1],"\t\t",i[2],"\t\t\t", "$", i[3],"\t\t\t", "$", i[4])
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Your VAT cost is $", VAT_AMT)
    print("Grand Total: $" + str(grand_total))

    # Write the purchase receipt to a file               
    file = open(str(name)+".txt","w")
    file.write("\n")
    file.write("\t \t \t \t \t laptop shop bill \n")
    file.write("\n")
    file.write("\t \t kamalpokhari, kathmandu | Phone No: 9849408157 \n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("laptop details are: \n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("Name of Customer:" + str(name) + "\n")
    file.write("Contact number: " +str(phone) + "\n")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Item Name \t\t Brand \t\t Total Quantity \t\t Unit Price \t\t Total" + "\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------\n")
    for i in user_purchased_laptops:
                    
        file.write(str(i[0])+ "\t\t " + str(i[1])+"\t\t"+str(i[2])+"\t\t\t " +str(i[3]) +  "\t\t\t"+ "$"+str(i[4])+"\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Your VAT is:" + "" +str(VAT_AMT)+"\n")
    file.write("\n")
    file.write("Grand Total : $" +str(grand_total)+"\n")
    file.write("\n")
    file.close()

# Function to generate the sales receipt
def sales_receipt(user_purchased_laptops,name,phone):
    total = 0
    shipping_cost = 500
    # Calculate the total price of sold laptops
    for i in user_purchased_laptops:
                 
        total =total+ int(i[4])
    grand_total = total+shipping_cost
                

    # Print the sales receipt           
    print("\n")
    print("\t \t \t bill")
    print("\n")
    print("\t \t Kamalpokhari, Kathmandu | Phone No: 9849408157")
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("laptop details are:")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Name of customer:" + str(name))
    print("Contact number:" +str(phone))
                 
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Purchase Details are:")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Item Name \t\t Brand \t\t Total Quantity \t\t Unit Price \t\t Total")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    for i in user_purchased_laptops:
                    
        print(i[0],"\t", i[1],"\t\t",i[2],"\t\t\t", i[3],"\t\t\t", "$", i[4])
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Your shipping cost is $", shipping_cost)
    print("Grand Total: $" + str(grand_total))

    # Write the sales receipt to a file            
    file = open(str(name)+".txt","w")
    file.write("\n")
    file.write("\t \t \t \t \t  bill \n")
    file.write("\n")
    file.write("\t \t Kamalpokhari, Kathmandu | Phone No: 9849408157 \n")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("laptop details are: \n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("Name of Customer: " + str(name) + "\n")
    file.write("Contact number: " +str(phone) + "\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Item Name \t\t Brand \t\t Total Quantity \t\t Unit Price \t\t Total" + "\n")
    file.write("---------------------------------------------------------------------------------------------------------------------------------------\n")
    for i in user_purchased_laptops:
                      
        file.write(str(i[0])+"\t\t "+str(i[1])+"\t\t "+str(i[2])+"\t\t\t " +str(i[3]) + "\t\t\t" + "$"+str(i[4])+"\n")
    file.write("-----------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Your shipping cost is:" + "" +str(shipping_cost)+"\n")
    file.write("\n")
    file.write("Grand Total : $" +str(grand_total)+"\n")
    file.write("\n")      
    file.close()
