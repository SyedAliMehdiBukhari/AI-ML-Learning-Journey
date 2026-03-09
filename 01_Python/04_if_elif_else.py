score = int(input("Apka score kya hai:"))
if score <50 and score >0:
    print("Rank: Bronze")
elif score <100 and score >=50:
    print("Rank: Silver")
elif score >= 100:
    print("Rank: Gold")
else:
    print("Invalid score")