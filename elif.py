moon_phase = "full moon"
if moon_phase == "full moon":
    print("Beware of werewolves!")
elif moon_phase == "new moon":
    print("Witches' night out")





potion_strength = 15
if potion_strength > 20:
    print("It's a super potent potion!")
elif potion_strength > 10:
    print("It's a moderately potent potion!")





weather = "rainy"
if weather == "sunny":
    print("It's a bright and beautiful day!")
elif weather == "rainy":
    print("Carry an umbrella!")
elif weather == "snowy":
    print("Time to build a snowman!")




sword_material = "silver"
if sword_material == "gold":
    print("The sword shines brightly!")
elif sword_material == "silver":
    print("The sword has a mystical glimmer!")
elif sword_material == "bronze":
    print("The sword looks ancient and valuable!")




player_level = 12
if player_level < 5:
    print("Access the beginner dungeon!")
elif 5 <= player_level < 10:
    print("Enter the intermediate dungeon!")
elif player_level >= 10:
    print("Challenge the advanced dungeon!")





is_dragon_present = True
has_treasure = False
if is_dragon_present and not has_treasure:
    print("Enter with caution! Dragon ahead, but no treasure in sight!")
elif not is_dragon_present and has_treasure:
    print("No dragon around! Quick, grab the treasure.")
elif is_dragon_present and has_treasure:
    print("A mighty dragon guards the treasure! Tread carefully.")
else:
    print("Empty lair. Safr to exlore, but no treasure here.")