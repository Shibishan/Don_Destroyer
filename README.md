# Don_Destroyer
This is a Python-based number battle game where the player faces enemies by selecting numbers. The player’s goal is to survive multiple attempts while ensuring the selected number is lower than DON’s life score. The game dynamically adjusts difficulty and saves game history for reference.

Features & Implementation Details:
User Input & Game Start:

The game begins by asking the player to enter their name.
A random life score (between 1 and 50) is assigned to DON (the enemy).
Game Loop & Number Selection:

The player faces 20 attempts, with each round presenting five randomly generated numbers.
The numbers are categorized into different ranges based on difficulty levels:
Attempts 1-5: (15 - 100)
Attempts 6-10: (250 - 2000)
Attempts 11-15: (3000 - 10000)
Attempts 16-20: (20000 - 100000)
The player selects a number from the displayed list.
Game Rules & Winning Condition:

If the chosen number is not in the list, the game ends with a defeat message.
If the chosen number is higher than DON’s life score, the game ends, and the player loses.
If the chosen number is lower than DON’s life score, the number gets added to DON’s life score, and the game continues.
If the player survives all 20 attempts, they win the game.
Game History & File Handling:

Every action and game status update is recorded in a list.
After game completion, the history is saved to a text file with a unique timestamp-based filename.
Technologies & Libraries Used:
Python Standard Library: Used for basic input handling and logic flow.
Random Module: Used to generate random numbers for enemy values and DON’s life score.
Datetime Module: Used to generate unique filenames for saved game history.
File Handling: The game history is stored in dynamically named .txt files for each session

