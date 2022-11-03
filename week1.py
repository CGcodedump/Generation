
#! Week One

products_list = ["Coke Zero", "Dr. Pepper", "Sprite", "Fanta"]

main_menu = '''
    Please choose from the following:
    
    [1]: Products Menu
    [0]: Exit
'''

product_menu = '''
    Please choose from the following:
    
    [1]: Products List
    [2]: Create New Product
    [3]: Update Existing Product
    [4]: Delete Product
    [0]: Return to main menu
'''
app = True

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

