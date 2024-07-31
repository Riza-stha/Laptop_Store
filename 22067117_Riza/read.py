#function to store data in a dictionary
def stored_in_dictionary():
    file = open("laptop_data.txt", "r")
    l_data ={}
    i_d=1
    for lines in file:
        lines = lines.replace("\n","")
        l_data.update({i_d:lines.split(",")})# Each line is split by ',' and stored as a list value in the dictionary
        i_d=i_d+1
    file.close()
    return l_data  # Returns the dictionary containing laptop data

#function to display the available stocks
def display_stock():
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N. \t\t Laptop Name       Company Name     \t\tPrice\t\tQuantity\tProcessor\t\tGraphics Card")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    file = open("laptop_data.txt", "r")
    i_d = 1
    for lines in file:
        print(i_d, "\t\t" + lines.replace(",","\t\t"))
        i_d=i_d+1
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")
