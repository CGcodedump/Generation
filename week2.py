
#! Week Two

app = True

products_list = ["Coke Zero", "Dr. Pepper", "Sprite", "Fanta"]

main_menu = '''Please choose from the following:
    
    [1]: Products Menu
    [2]: Orders Menu
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

    [1]: Print Orders
    [2]: Create New Order
    [3]: Update Order Status
    [4]: Edit Existing Order Details
    [5]: Delete Order
    [0]: Exit
"""

list_of_orders = [
    {"Customer Name": "John", "Customer Address": "Unit 2, 12 main street, London, WH1 2ER", "Customer Phone": "0789887334", "Status": "PREPARING"}, 
    {"Customer Name": "John", "Customer Address": "Unit 2, 12 main street, London, WH1 2ER", "Customer Phone": "0789887334", "Status": "DELIVERY"}, 
    {"Customer Name": "John", "Customer Address": "Unit 2, 12 main street, London, WH1 2ER", "Customer Phone": "0789887334", "Status": "DELIVERED"}
    ]

order = {}

while app == True:
    try:
        print (main_menu)
        user_input = int(input("\nInput a number: "))
    except ValueError:
        print("ERROR: Input a number shown")
    else:
        if user_input == 0:
            print("\nThanks for using the app")
            break
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
                    break