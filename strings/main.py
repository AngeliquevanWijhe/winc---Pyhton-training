# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player = "Ruud Gullit"
player_0 = "Marco van Basten"
scorer_0 = player
scorer_1 = player_0
goal_0 = 32
goal_1 = 54
scorers = f"{scorer_0} {goal_0}, {scorer_1} {goal_1}"
report = f"{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute"
print (report)
first_name = f"{player[:4]}"
last_name_len = len(player[player.find(" ") + 1:])
name_short = f"{player[0]}. {player[player.find(' ') + 1:]}"
chant_0 = f"{first_name}! " * len(first_name)
good_chant = chant_0[:-1] != " "
chant = chant_0[:-1]  # remove the trailing space
print (first_name)
print (last_name_len)
print (name_short)
print (chant)
print (good_chant)
print (chant_0[-1])