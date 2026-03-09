while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is: {result}")
        break  # Exit the loop if the operation is successful
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please enter a non-zero number.")