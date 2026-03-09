def calculate_discount(price, discount_percent):
    discount_value = (price * discount_percent) / 100
    discounted_price = price - discount_value
    return discounted_price

original_price = float(input("Original Price batao:"))

final_price = calculate_discount(original_price, 20)
print(f"Final Price after 20% discount: {final_price}")