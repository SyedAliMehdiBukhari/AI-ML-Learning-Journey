total_xp = int(input("Total XP kitna hai: "))
remaining_xp_for_level_up = 100 - total_xp
if total_xp >= 100:
    print("Congratulations! Level Up! You are now level 2")
else:
    print(f"Level Up hone ke liye {remaining_xp_for_level_up} XP aur chaiye")