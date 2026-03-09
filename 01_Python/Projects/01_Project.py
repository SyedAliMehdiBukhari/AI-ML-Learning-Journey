# Project Name: The Warehouse Manager

inventory = []

# Calculate total prices of Mobile in Inventory
def inventory_price_calculator(): 
    total_price = 0
    for item in inventory:
        total_price += item["Price"]
    return total_price
    
# Add new mobile to inventory
def add_mobile_to_inventory(brand, model, price):
    mobile = {"Brand": brand,
                   "Model": model,
                   "Price": price}
    inventory.append(mobile)
    print(f"Added {brand} {model} to inventory.")
    
# View all mobiles in inventory
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Mobiles in Inventory:")
        for item in inventory:
            print(f"{item['Brand']} | {item['Model']} | Rs: {item['Price']}")
            
# Check total price of inventory
def check_total_inventory_price():
    total_price = inventory_price_calculator()
    print(f"Total Price of Inventory: Rs {total_price}")
    
# Main function to run the warehouse manager
def main():
    while True:
        print("\nWarehouse Manager")
        print("1. Add Mobile to Inventory")
        print("2. View Inventory")
        print("3. Check Total Inventory Price")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                brand = input("Enter Mobile Brand: ")
                model = input("Enter Mobile Model: ")
                price = int(input("Enter Mobile Price: "))
                add_mobile_to_inventory(brand, model, price)
            case "2":
                view_inventory()
            case "3":
                check_total_inventory_price()
            case "4":
                print("Goodbye!")
                break
            
if __name__ == "__main__":
    main()