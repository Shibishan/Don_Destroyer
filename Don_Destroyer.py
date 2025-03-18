import random
import datetime

# Declare variables
user_name = ""
user_score = 0
max_attempts = 20
score_ranges = [(15, 100), (250, 2000), (3000, 10000), (20000, 100000)]
game_history = []
num_list = 0

def play_game():
    """
    Plays the game where the user fights enemies with randomly generated numbers.

    The goal is to select a number that is less than DON's life score to defeat the enemies and survive the attempts.
    """
    # Getting input from user as user's name
    user_name = input("Enter your name: ")

    # Generate a one-time random "Life Score" for DON
    don_life_score = random.randint(1, 50)
    print("\nPlayer Name:", user_name)

    # Loop through the maximum attempts
    for attempt in range(1, max_attempts + 1):
        # Set the range of numbers based on the attempt number
        if attempt <= 5:
            min_val, max_val = score_ranges[0]
        elif attempt <= 10:
            min_val, max_val = score_ranges[1]
        elif attempt <= 15:
            min_val, max_val = score_ranges[2]
        else:
            min_val, max_val = score_ranges[3]

        # Generate 5 random numbers within the range
        enemy_numbers = [random.randint(min_val, max_val) for _ in range(5)]

        print(f"\nAttempt: {attempt}")
        print(f"{user_name}'s life score is: {don_life_score}")
        num_list = " ".join(map(str, enemy_numbers))
        print(num_list)

        # Get the user's input
        chosen_enemy = input("Select a number to fight: ")

        # Check if the chosen number is valid
        if not chosen_enemy.isdigit() or int(chosen_enemy) not in enemy_numbers:
            print("No such enemy")
            print(f"\n*** Game status ***\nPlayer name: {user_name}\nTotal attempts: {attempt}\nFinal life score: {don_life_score}\n{user_name} was defeated !!!")
            game_history.append(f"\nAttempt: {attempt}\n{user_name}'s life score is: {don_life_score}\n{num_list}\nSelected Number: {chosen_enemy}\nNo Such Enemy")
            game_history.append(f"\n*** Game status ***\nPlayer name: {user_name}\nTotal attempts: {attempt}\nFinal life score: {don_life_score}\n{user_name} was defeated !!!")
            now = datetime.datetime.now()
            filename = now.strftime('%Y_%m_%d_%H_%M_%S') + "_" + str(random.randint(0, 9999)) + ".txt"
            with open(filename, 'a') as file:
                file.write('\n'.join(game_history))
            break

        chosen_enemy = int(chosen_enemy)
        # Check if the chosen number is higher than DON's "Life Score"
        if chosen_enemy > don_life_score:
            print(f"{chosen_enemy} killed {user_name}")
            print(f"\n*** Game status ***\nPlayer name: {user_name}\nTotal attempts: {attempt}\nFinal life score: {don_life_score}\n{user_name} was defeated !!!")
            game_history.append(f"{user_name}'s life score is: {don_life_score}\n{num_list}\nSelected Number: {chosen_enemy}\n{chosen_enemy} killed {user_name}")
            game_history.append(f"\n*** Game status ***\nPlayer name: {user_name}\nTotal attempts: {attempt}\nFinal life score: {don_life_score}\n{user_name} was defeated !!!")
            now = datetime.datetime.now()
            filename = now.strftime('%Y_%m_%d_%H_%M_%S') + "_" + str(random.randint(0, 9999)) + ".txt"
            with open(filename, 'a') as file:
                file.write('\n'.join(game_history))
            break

        # Add the chosen number to DON's "Life Score"
        don_life_score += chosen_enemy
        print(f"{user_name} killed {chosen_enemy}")
        game_history.append(f"\nAttempt: {attempt}\n{user_name}'s life score is: {don_life_score}\n{num_list}\n{user_name} killed {chosen_enemy}")

    else:
        print(f"\n*** Game status ***\nPlayer name: {user_name}\nTotal attempts: {max_attempts}\nFinal score: {don_life_score}\n{user_name} saved letter-kind")
        game_history.append(f"\n*** Game status ***\nPlayer name: {user_name}\nTotal attempts: {max_attempts}\nFinal score: {don_life_score}\n{user_name} saved letter-kind")

    # Save game history to a text file
    now = datetime.datetime.now()
    filename = now.strftime('%Y_%m_%d_%H_%M_%S') + "_" + str(random.randint(0, 9999)) + ".txt"
    with open(filename, 'w') as file:
        file.write('\n'.join(game_history))

# Calling the Function
play_game()
