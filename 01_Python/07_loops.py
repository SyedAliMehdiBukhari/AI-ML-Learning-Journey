#Problem 1: Loop with a list of phone brands

# brands = ["Samsung", "Apple", "Xiaomi", "Oppo", "Vivo"]

# for brand in brands:
#     print(f"{brand} is available in store.")
    
# print("Stock check complete")

#Problem 2: Loop with if condition

# prices = [12000, 45000, 5000, 80000, 15000, 30000]
# prices.sort()

# for price in prices:
#     if price > 20000:
#         print(f"High Budget: {price}")
        
# print("Scanning Complete")

#Problem 3: For Loop

# sales = [5000, 2000, 10000, 3000, 500]
# total_sales = 0

# for sale in sales:
#     total_sales += sale
    
# print(f"Total Sales: {total_sales}")

#Problem 4: While Loop

correct_pin = 1234
user_pin = 0
attempts = 0

while True:
    user_pin = int(input("Enter 4-digit PIN: "))
    attempts += 1
    
    if user_pin != correct_pin and attempts < 3:
        print("Incorrect PIN. Try again.")
    elif user_pin == correct_pin:
        print("PIN accepted. Access granted.")
        break
    if attempts == 3:
        print("Card Blocked! Too many attempts")
        break
        
