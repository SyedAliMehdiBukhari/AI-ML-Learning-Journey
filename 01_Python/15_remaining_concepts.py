# *args

# def flexible_calculator(operation, *numbers):
#     if operation == "add":
#         return sum(numbers)
#     elif operation == "subtract":
#         result = numbers[0]
#         for num in numbers:
#             result -= num
#         return result
#     elif operation == "multiply":
#         result = 1
#         for num in numbers:
#             result *= num
#         return result
#     elif operation == "divide":
#         result = numbers[0]
#         for num in numbers[1:]:
#             if num == 0:
#                 return "Error: Division by zero"
#             result /= num
#         return result
    
# addition = flexible_calculator("add", 1, 2, 3)        # Output: 6
# subtraction = flexible_calculator("subtract", 10, 5, 2)   # Output: -17
# multiplication = flexible_calculator("multiply", 2, 3, 4)    # Output: 24
# division = flexible_calculator("divide", 100, 5, 2)    # Output: 10.0

# print("Addition:", addition)
# print("Subtraction:", subtraction)  
# print("Multiplication:", multiplication)
# print("Division:", division)

# Lambda Function # Use to write short functions in 1 Line

# def cube(number)
#    return number**3 

# same as 

cube = lambda number : number**3

# print(cube(5))

# Map Function # Use to change or manipulate list 

# basically ye har element par ek function apply karta hai

l = [1,2,3,4,5]

new_list = list(map(cube, l))

print(new_list)

# Filter Function # Use to filter values in list, set, tuples etc

def filter_small_values(value):
    return value > 2

new_list_2 = list(filter(filter_small_values, l))

print(new_list_2)

# List Comprehension # Basically Map and Filter ek hi line me kr leti hai

result = [x**2 for x in l if x % 2 == 0]

print(result)
