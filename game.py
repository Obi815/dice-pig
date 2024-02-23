import random

# Make the random dice roll 
def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll 
value = roll()

# set up players 
while True:
    players = input("Enter the number of player (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print("Lets Begin!!!")
            break
        else:
            print("Try Again...")
    else:
        print("Must be a valid number between (2-4)")
print(players)

max_score = 20
players_scores = [0 for _ in range(players)]

print(players_scores)

