emails = ["ali@test.com", "user@test.com", "ali@test.com", "admin@test.com", "user@test.com"]  # list with duplicate values

unique_emails = set(emails)  # converting list to set to remove duplicates

print(f"Unique Emails: {unique_emails}, \nLength of Unique Emails: {len(unique_emails)}")  # Output

if "admin@test.com" in unique_emails:
    print("Admin Found")