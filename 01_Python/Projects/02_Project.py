# -------------- Secure Banking System --------------

import random
import datetime

authorized_users = ("ali", "manager", "admin")
transaction_ids = set()

def login_system(username):
    if username not in authorized_users:
        print("------------")
        print("Acess Denied")
        print("------------")
        return False
    else:
        print("------------")
        print(f"Welcome, {username.capitalize()}!")
        print("------------")
        return True
        
def deposit_money(*amounts):
    total = sum(amounts)
    tax = total * 0.1  # 10% tax
    global final_amount
    final_amount = total - tax
    print("------------")
    print(f"{final_amount} deposited into your account")
    print("------------")
    save_to_file()
    

def save_to_file():
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    transaction_data = f"ID: {generate_transaction_id()} | Time: {time_now} | Amount Deposited: {final_amount} \n"
    with open("Bank_Records.txt" ,"a") as file:
        file.write(transaction_data)
    

def generate_transaction_id():
    while True:
        transaction_id = random.randint(1000, 9999)
        if transaction_id not in transaction_ids:
            transaction_ids.add(transaction_id)
            return transaction_id
    

def main():
    print("---------- Welcome to Secure Bank ----------")
    username = input("Enter the account username: ")
    try:
        login_approved = login_system(username.lower())
        if login_approved:
            amount_to_deposit = input(f"What amount you want to deposit {username} ")
            deposit_money(float(amount_to_deposit))
    except:
        print("Something went wrong")
    
if __name__ == "__main__":
    main()
    