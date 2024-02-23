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


max_score = 20
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn.\n")
        print("Your score is:", players_scores[player_idx])
        current_score = 0 

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1... TURN OVER")
                current_score = 0
                break
            else:
                current_score += value
                print("Your rolled a: ", value)

            print("Your score is: ", current_score)

        players_scores[player_idx] += current_score
        print("Your total score is:", players_scores[player_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with the score of:", max_score)




