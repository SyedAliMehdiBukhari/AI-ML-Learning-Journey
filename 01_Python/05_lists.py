#Problem 1:

# phones = ["iPhone 13", "Samsung S21", "Pixel 6"]
# print(f"Current Stock: {phones}")
# new_phone = input("Naya phone stock me add karna hai? Name batao: ")
# phones.append(new_phone)
# print(f"Updated Stock: {phones}")

#Problem 2:

# phones = ["iPhone 13", "Samsung S21", "Pixel 6"]
# print(f"Second Phone is: {phones[1]}")
# phones[2] = "Pixel 7"
# print(f"Updated Stock: {phones}")

#Problem 3:

# stock = ["Nokia", "Samsung", "iPhone", "Xiaomi", "Oppo"]
# print(f"Original Stock: {stock}")
# stock.pop()
# stock.remove("iPhone")
# print(f"Remaining Stock: {stock}")

#Problem 4:

# prices = [5000, 10000, 15000, 20000, 25000, 30000, 35000]
# budget = prices[0:3]
# premium = prices[-3:]
# print(f"Budget Phones: {budget}")
# print(f"Premium Phones: {premium}")

#Problem 5: #List Comprehension

prices = [100, 200, 300, 400, 500]

new_prices = [price * 2 for price in prices if price > 300]

print(f"New Prices: {new_prices}")
