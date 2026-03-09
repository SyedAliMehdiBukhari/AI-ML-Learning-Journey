raw_data = " Player1,Level_5,Score_5000 "

raw_data = raw_data.strip()
print(raw_data)

raw_data_list = raw_data.split(",")
print(raw_data_list)

player_name, level, score = raw_data_list
print(f"Player Name: {player_name}")
print(f"Level: {level}")
print(f"Score: {score}")