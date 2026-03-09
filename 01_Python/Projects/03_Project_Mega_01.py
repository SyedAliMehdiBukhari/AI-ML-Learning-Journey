# --------------- The Digital Mart: Inventory & Sales System ---------------
# --------------------------------------------------------------------------

# Import

from datetime import datetime 

# Program

admins = ("ali", "naqi", "shani")   # Authorized Persons or Admins 

customers = set()           # Empty Set for Adding Unique Customers

inventory_storage = {}      # Empty Dictionary for Inventory Storage 

# Read Products from Products Txt File and Store in Inventory Storage Dictionary
def inventory_checker():
    
    try:
        # Getting Products from Warehouse
        with open("products_in_warehouse.txt", "r") as inventory:
            product_list = inventory.readlines()
        
        # Adding Products to Inventory Storage
        for product in product_list:
            product_name, product_price, product_stock = product.strip().lower().split(",")
            inventory_storage.update({product_name:[product_price, product_stock]})

    except:
        print("Products Inventory not found")

# Check Login Credentials if person is Admin or Customer          
def logic_person_credentials_check(username):
    
    # Checks if User is Admin or Customer
    if username in admins:
        # Show Admin Panel Menu
        admin_panel(username)
        
    else:
        # Add Customer to Set()
        customers.add(username)
        
        # Show Customer Shopping Panel Menu
        shopping_menu(customer_name = username)
  
# If User is Customer then this Function (Shopping Menu) will be called    
def shopping_menu(customer_name):
    
    total_cart_to_calculate = None
    
    print("--------------------------------------------------")
    print(f"Dear {customer_name.capitalize()}! You can choose")
    print("--------------------------------------------------")
    print("Option 1 to View Available Products")
    print("Option 2 for Adding Product to Cart")
    print("Option 3 to Checkout")
    print("Option 4 to Exit Shoping Menu")
    
    while True:
        
        try:
            
            print("--------------------------------------------------")
            
            choice = int(input(f"What you want to do {customer_name.capitalize()} Sir! "))
            
            # Choice Based Operations
            # -----------------------
            
            match choice:
                
                # Option 1 - View/Show Available Products
                case 1:
                    show_available_products()
                    
                # Option 2 - Add Products to Cart
                case 2:
                    total_cart_to_calculate = add_products_to_cart()
                
                # Option 3 - Checkout (Pay Bill or Discard)
                case 3:
   
                    if total_cart_to_calculate == None:
                        print("--------------------------------------------------") 
                        print("Shopping Cart is Empty")
                    else:
                        calculate_total_cart(customer_name, total_cart_to_calculate)                   
    
                # Option 4 - Exit Shopping Menu
                case 4:
                    print("--------------------------------------------------") 
                    print(f"Have a good day! {customer_name.capitalize()}")
                    print("--------------------------------------------------") 
                    return        
            
        except ValueError:    
            print("Sir! Please choose valid option")

# Show Available Products in Digital Mart Warehouse
def show_available_products():
    
    i = 1
    print("--------------------------------------------------")
    print(f"Available Products are: ")
    
    # Show Products
    for product_name in inventory_storage.keys():   
        print(f"{i}. {product_name.capitalize()}")
        i += 1

# Add Products to Cart   
def add_products_to_cart():
    
    # List to Store Customer Shopping Cart
    
    total_shopping_cart_list = []   # Use to further Calculate Checkout
    
    total_cart = shopping_cart()
    
    try:
        
        while True:
            
            # Adding Shopping Cart Dictionary to  Total Shooping List
            total_shopping_cart_list.append(total_cart) 
        
            print("--------------------------------------------------")
        
            continue_shopping = input("Do you want to shop more? Y/N: ").lower()
    
            if continue_shopping == 'y':
            
                total_cart = shopping_cart()
            
            elif continue_shopping == 'n':
                return total_shopping_cart_list
        
            else:
                print("--------------------------------------------------")
                print("Enter valid option")
                return total_shopping_cart_list
            
    except ValueError:
        print("Enter valid choice")
               

def shopping_cart():
          
    shopping_cart = {}
    
    try:
            
        # No of Products user want to Add to Cart
        
        print("--------------------------------------------------")
            
        total_products = int(input("Sir! How many Products do you want to Add to your Cart: "))
                
        for shop_product in range(total_products):
            
            print("--------------------------------------------------")
                    
            product = input("Enter Product name to add into your shopping cart: ").strip().lower()
                    
            if product in inventory_storage.keys():
                            
                # Getting Product Price and Stock
                product_price , product_stock = inventory_storage.get(product) # It will return list [price,stock]
                product_price = int(product_price)
                product_stock = int(product_stock)
                            
                # Add to Shopping Cart (If we have stock)
                if product_stock >= 1:
                    shopping_cart.update({product: product_price})
                    print("--------------------------------------------------")
                    print(f"{product.capitalize()} with Price: Rs.{product_price:,} Added to Cart")
                else:
                    print("--------------------------------------------------")
                    print(f"Sorry Sir! {product.capitalize()} is out of stock")
                                
            else:
                print("--------------------------------------------------")
                print(f"Sorry Sir! {product.capitalize()} not available right now")
                
        return shopping_cart 
            
    except ValueError:   
        print("--------------------------------------------------") 
        print("Please enter valid product name")

# Calculate Total Price of products in Cart       
def calculate_total_cart(user_name, total_cart_list):
    
    total_products_price = 0
    
    print("--------------------------------------------------") 
    print("Total Products in cart: ")
    
    # Accessing List of Dictionary
    for product_name_and_prices in total_cart_list:      # Returns Dictionaries with Product Name and Price   
        for product_name, product_price in product_name_and_prices.items():
            # Calculate Products Price
            total_products_price += product_price 
            print(f"{product_name.capitalize()} Rs. {product_price:,}") 
            
    # Calculate 5% Tax on Products Below Rs.2000 and 10% Tax on Above Rs.2000
    
    total_tax = lambda product_price: product_price * 0.05 if product_price < 2000 else product_price * 0.1
    
    total_price = total_products_price + total_tax(total_products_price)
    
    print(f"Products Cost: Rs.{total_products_price:,} + Tax: {total_tax(total_products_price)} : Total Price: {total_price:,}")
    
    if total_price > 0:
        
        while True:    
            
            print("--------------------------------------------------")
            checkout_or_discard = input("Do you want to checkout? Y/N: ").lower()
        
            if checkout_or_discard != 'y' and checkout_or_discard != 'n':
                print("--------------------------------------------------")
                print("Invalid choice")
                
            else:
                if checkout_or_discard == 'y':
                
                    # checkout()
                    checkout(user_name, total_price)
                    return
                
                elif checkout_or_discard == 'n':
                    return      

# Checkout and Record data in (sales_record) File             
def checkout(user_name, total_price):
    
    payment_method = ''
    
    print("--------------------------------------------------")
    print("You want to pay through Cash or Credit Card?")
    
    while True:
        
        try:
        
            print("--------------------------------------------------")
            payment_choice = int(input("Option 1 : Cash\nOption 2 : Credit Card "))     # Returns Integer 
    
            # 1 - Cash , 2- Credit Cash

            if payment_choice == 1:
                payment_method = "Cash"
                
            elif payment_choice == 2:
                payment_method = "Credit Card"
                
            else:
                print("--------------------------------------------------")
                print("Enter Valid Choice ")
                
            time = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    
            sales_record = f"{time} | User: {user_name.capitalize()} | Payment Method: {payment_method} | Total: Rs.{total_price}\n"
    
            # Write Sales Record
    
            with open("sales_log.txt", "a") as record:
                record.write(sales_record)
                
            return   
            
        except ValueError:
            print("--------------------------------------------------")
            print("Enter Valid Choice ")
            
def admin_panel(admin_name):
    
    record_list = []
    
    print("--------------------------------------------------")
    print(f"{admin_name.capitalize()}! what you want to do?")
    print("Option 1 to View All Sales Record")
    print("Option 2 to View High Value Orders")
    print("Option 3 to Exit")
    
    while True:
        
        try:
                    
    
            print("--------------------------------------------------")
            choice = int(input("Enter your choice: "))
    
            match choice:
                
            # Option 1 - View All Sales Record
                case 1:
                    # Read Sales Record File
                    with open("sales_log.txt", "r") as sales_record:
                        record_list = sales_record.readlines()
                           
                    for record in record_list:
                        print("--------------------------------------------------")
                        print(record)
            
            # Option 2 - View High Value Order / Sales
                case 2:
                    for record in record_list:
                        pass
                                 
            # Option 3 - Exit
                case 3:
                    print("Have a good day!")
                    return
        
        except ValueError:
            print("Sir! Please choose valid option")
    
def main():
    
    print("\n")
    print("------------------------------ Welcome -----------------------------------")
    print("-------------------------------- to --------------------------------------")
    print("-------------------------- The Digital Mart ------------------------------")
    print("\n")
    user_name = input("Enter your good name: ").lower()
    inventory_checker()
    logic_person_credentials_check(user_name)
        
if __name__ == "__main__":
    main()
        
    