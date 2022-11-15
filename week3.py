
#! Week Three

app = True

products_list = []
courier_list = []

def prodSave():
    with open('products.txt', 'w') as filehandle:
        for listitem in products_list:
            filehandle.write(f'{listitem}\n')

def prodLoad():
    with open('products.txt', 'r') as filehandle:
        for line in filehandle:
            # Remove linebreak which is the last character of the string
            prod_file = line[:-1]
            # Add item to the list
            products_list.append(prod_file)

def courSave():
    with open('couriers.txt', 'w') as filehandle:
        for listitem in courier_list:
            filehandle.write(f'{listitem}\n')

def courLoad():
    with open('couriers.txt', 'r') as filehandle:
        for line in filehandle:
            # Remove linebreak which is the last character of the string
            cour_file = line[:-1]
            # Add item to the list
            courier_list.append(cour_file)

main_menu = '''Please choose from the following:
    
    [1]: Products Menu
    [2]: Orders Menu
    [3]: Courier Menu
    [0]: Exit
'''

product_menu = '''Please choose from the following:
    
    [1]: Products List
    [2]: Create New Product
    [3]: Update Existing Product
    [4]: Delete Product
    [0]: Return to main menu
'''
order_menu = """Please choose from the following:

    [1]: Order List
    [2]: Create New Order
    [3]: Update Order Status
    [4]: Edit Existing Order Details
    [5]: Delete Order
    [0]: Return to main menu
"""
courier_menu = """Please choose from the following:

    [1]: Courier List
    [2]: Create New Courier
    [3]: Update Existing Courier
    [4]: Delete Courier
    [0]: Return to main menu
"""

list_of_orders = [
    {"Customer Name": "John", "Customer Address": "Unit 2, 12 main street, London, WH1 2ER", "Customer Phone": "0789887334", "Status": "PREPARING"}, 
    {"Customer Name": "John", "Customer Address": "Unit 2, 12 main street, London, WH1 2ER", "Customer Phone": "0789887334", "Status": "DELIVERY"}, 
    {"Customer Name": "John", "Customer Address": "Unit 2, 12 main street, London, WH1 2ER", "Customer Phone": "0789887334", "Status": "DELIVERED"}
    ]

order = {}

prodLoad()
courLoad()


while app == True:
    try:
        print (main_menu)
        user_input = int(input("\nInput a number: "))
    except ValueError:
        print("ERROR: Input a number shown")
    else:
        if user_input == 0:
            print("\nThanks for using the app")
            prodSave()
            courSave()
            break

        #! Product Menu
        elif user_input == 1:
            try:
                print(product_menu)
                user_input = int(input("\nChoose an option: "))
            except ValueError:
                print("ERROR: Input a number shown")
            else:
                if user_input == 0:
                    print("\nReturning to the main menu")

                elif user_input == 1:
                    print("\nThe current list is: \n")
                    print(*products_list, sep=", ")

                elif user_input == 2:
                    new_product = input("\nAdd a new product to the list: ")
                    products_list.append(new_product)
                    print (f"\nYou've added {new_product} to the list")

                elif user_input == 3:
                    print("\nExisting products and the index values\n")
                    for index, value in enumerate(products_list):
                        print(index, value)

                    index_select = int(input("\nSelect which product you'd like to edit: "))
                    new_value = input("\nNew product name: ")
                    products_list[index_select] = new_value

                elif user_input == 4:
                    print("\nExisting products and the index values\n")
                    for index, value in enumerate(products_list):
                        print(index, value)

                    prod_del = int(input("\nSelect which product you'd like to delete: "))
                    products_list.pop(prod_del)

        #! Order Menu
        elif user_input == 2:
            try:
                print(order_menu)
                user_input = int(input("Input a number: "))
            except ValueError:
                print("ERROR: Input a number shown")
            else:
                if user_input == 1:
                    for index, value in enumerate(list_of_orders):                        
                        print(index, value, sep=": ")
                elif user_input == 2:
                    order["Customer Name"] = input("Enter a name: ")
                    order["Customer Address"] = input("Enter an address: ")
                    order["Customer Phone"] = input("Enter a phone number: ")
                    for index, value in enumerate(courier_list):                        
                        print(index, value, sep=": ",)
                    courier_choice = int(input("Which courier would you like: "))
                    order["Courier"] = courier_list[courier_choice]
                    order["Status"] = "PREPARING"
                    print(order)
                    list_of_orders.append(order)
                elif user_input == 3:
                    print("Update order status test")
                    for index, value in enumerate(list_of_orders):                        
                        print(index, value, sep=": ",)
                    order_status_index = int(input("Which item would you like to edit? "))
                    order_status_edit = input("What is the status of the order? ")
                    list_of_orders[order_status_index]["Status"] = order_status_edit
                elif user_input == 4:
                    print("Update existing order test")
                    for index, value in enumerate(list_of_orders):                        
                        print(index, value, sep=": ",)
                    update_order_index = int(input("Which item would you like to edit? "))
                    for x, y in list_of_orders[update_order_index].items():                        
                        updateName = input("Would you like to change the name? (Leave blank to skip) ")
                        if updateName == "":
                            print("Left blank, skipping")
                        else:
                            list_of_orders[update_order_index]["Customer Name"] = updateName
                            print(f"New name is: {list_of_orders[update_order_index]['Customer Name']}")
                        updateAddress = input("Would you like to change the address? (Leave blank to skip) ")
                        if updateAddress == "":
                            print("Left blank, skipping")
                        else:
                            list_of_orders[update_order_index]["Customer Address"] = updateAddress
                            print(f"New address is: {list_of_orders[update_order_index]['Customer Address']}")
                        updatePhone = input("Would you like to change the phone number? (Leave blank to skip) ")
                        if updatePhone == "":
                            print("Left blank, skipping")
                        else:
                            list_of_orders[update_order_index]["Customer Phone"] = updatePhone
                            print(f"New phone number is: {list_of_orders[update_order_index]['Customer Phone']}")
                        updateStatus = input("Would you like to change the order status? (Leave blank to skip) ")
                        if updateStatus == "":
                            print("Left blank, skipping")
                            break
                        else:
                            list_of_orders[update_order_index]["Status"] = updateStatus
                            print(f"New order status is: {list_of_orders[update_order_index]['Status']}")
                            break
                elif user_input == 5:
                    for index, value in enumerate(list_of_orders):                        
                        print(index, value, sep=": ")
                    orderDel = int(input("Which order would you like to delete? "))
                    list_of_orders.pop(orderDel)
                elif user_input == 0:
                    print("Returning to main menu")
        
        #! Courier Menu
        elif user_input == 3:
            try:
                print(courier_menu)
                user_input = int(input("Input a number: "))
            except ValueError:
                print("ERROR: Input a number shown")
            else:
                #! 1: Print Courier List
                if user_input == 1:
                    print("\nThe current list is: \n")
                    for index, value in enumerate(courier_list):                        
                        print(index, value, sep=": ")
                elif user_input == 2:
                #! 2: Create new courier
                    new_courier = input("\nAdd a new product to the list: ")
                    courier_list.append(new_courier)
                    print (f"\nYou've added {new_courier} to the list")
                
                elif user_input == 3:
                #! 3: Update courier
                    print("\nExisting products and the index values\n")
                    for index, value in enumerate(courier_list):
                        print(index, value)
                    index_select = int(input("\nSelect which courier you'd like to edit: "))
                    new_value = input("\nNew courier name: ")
                    courier_list[index_select] = new_value
                
                elif user_input == 4:
                #! 4: Delete courier
                    print("\nExisting couriers and the index values\n")
                    for index, value in enumerate(courier_list):
                        print(index, value)
                    cour_del = int(input("\nSelect which product you'd like to delete: "))
                    courier_list.pop(cour_del)

                elif user_input == 0:
                #! 0: Return to main menu
                    print("Returning to main menu")
