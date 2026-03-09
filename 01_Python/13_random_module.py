import random

options = ["Heads", "Tails"]

computer_choice = random.choice(options)

user_choice = input("Choose Heads or Tails: 1 for Heads, 2 for Tails: ")

if user_choice == "1":
    user_choice = "Heads"
    
elif user_choice == "2":
    user_choice = "Tails"
    
else:
    print("Invalid choice. Please choose 1 for Heads or 2 for Tails.")
    
print(f"Computer choose: {computer_choice}")
print(f"You choose: {user_choice}")

if computer_choice == user_choice:
    print("You win!")
else:
    print("You lose!")