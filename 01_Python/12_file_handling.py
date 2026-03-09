#File handling in Python with datetime module

import datetime
user_diary_note = input("Ajj diary mein kya likhna hai? ")
time_now = datetime.datetime.now()
time_now = time_now.strftime("%Y-%m-%d %I:%M %p")
diary_note = f"{time_now}: {user_diary_note}"

with open("12_diary.txt", "a") as file:
    file.write(f"{diary_note} \n")
    
print("Note Added")
with open("12_diary.txt", "r") as file:
    content = file.read()
    print("--- Purani Diary ---")
    print(content)