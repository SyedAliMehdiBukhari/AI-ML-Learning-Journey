#Problem 1:

# mobile_spec = {"Brand": "Apple",
#                "Model": "iPhone 14",
#                "Price": 180000}

# print(f"Phone Model: {mobile_spec["Model"]}")
# mobile_spec["Price"] = 175000
# mobile_spec["Color"] = "Midnight Black"

# print(f"Updated Mobile Specifications: {mobile_spec}")

#Problem 2:

inventory = {"Apple": 150, "Banana": 50, "Milk": 200}

user_input = input("Apko Kya chahiye? (Apple, Banana, Milk): ")

if user_input in inventory:
    price = inventory.get(user_input, "Not Available")
    print(f"Price of {user_input}: {price}")
else:
    for item, price in inventory.items():
        print(f"We have: {item} for Rs {price}")
