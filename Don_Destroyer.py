import random
import datetime
import time
import sys

# =============================
# ✨ Helper Functions
# =============================

def type_text(text, delay=0.03):
    """Simulate smooth typing animation for better transitions."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slow_print(text, delay=0.5):
    """Print with a short delay for dramatic effect."""
    print(text)
    time.sleep(delay)

def loading_dots(message="Loading", dots=3, delay=0.4):
    """Simple dot loading animation."""
    print(message, end="")
    for _ in range(dots):
        time.sleep(delay)
        print(".", end="")
        sys.stdout.flush()
    print("\n")

def generate_filename():
    """Generate unique filename for game history."""
    now = datetime.datetime.now()
    return now.strftime("%Y_%m_%d_%H_%M_%S") + "_" + str(random.randint(0, 9999)) + ".txt"

def save_game_history(user_name, game_history):
    """Save game history with UTF-8 encoding (emoji-safe)."""
    filename = generate_filename()
    loading_dots("💾 Saving game history")
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(game_history))
    slow_print(f"📁 Game history saved successfully as: {filename}\n", 0.7)


# =============================
# ⚔️ Main Game Function
# =============================

def play_game():
    type_text("🔥 Welcome to THE DON BATTLE 🔥\n", 0.05)
    user_name = input("Enter your hero name: ").capitalize()

    # Random starting life score
    don_life_score = random.randint(50, 100)
    type_text(f"\n⚔️ Welcome, {user_name}! Your starting Life Score is {don_life_score}.\n", 0.04)

    max_attempts = 20
    score_ranges = [
        (10, 50), (50, 250), (250, 1000), (1000, 5000)
    ]

    game_history = []
    start_time = datetime.datetime.now()

    # =============================
    # 🎮 Game Loop
    # =============================
    for round_num in range(1, max_attempts + 1):
        # Pick range based on round
        if round_num <= 5:
            min_val, max_val = score_ranges[0]
        elif round_num <= 10:
            min_val, max_val = score_ranges[1]
        elif round_num <= 15:
            min_val, max_val = score_ranges[2]
        else:
            min_val, max_val = score_ranges[3]

        # Generate enemies
        enemies = [random.randint(min_val, max_val) for _ in range(5)]

        # Round intro animation
        type_text(f"\n⚡ Preparing for ROUND {round_num}...", 0.04)
        loading_dots("Summoning enemies", 4, 0.3)

        type_text(f"💖 {user_name}'s Life Score: {don_life_score}", 0.02)
        print("👹 Enemies:", "  ".join(map(str, enemies)))

        chosen = input("👉 Choose an enemy number to fight: ")

        # Validate input
        if not chosen.isdigit() or int(chosen) not in enemies:
            type_text("❌ Invalid choice! You picked an enemy that doesn’t exist.", 0.03)
            type_text(f"\n💀 {user_name} was defeated in Round {round_num}!", 0.03)
            game_history.append(f"Round {round_num}: Invalid enemy {chosen}. {user_name} defeated.")
            break

        chosen = int(chosen)

        # Battle logic
        if chosen > don_life_score:
            type_text(f"💀 {chosen} was too powerful! It defeated {user_name}.", 0.04)
            game_history.append(f"Round {round_num}: {chosen} defeated {user_name}. Final Life Score: {don_life_score}")
            break
        else:
            type_text(f"🔥 {user_name} defeated {chosen} and absorbed its power!", 0.03)
            don_life_score += chosen
            game_history.append(f"Round {round_num}: {user_name} defeated {chosen}. Life Score: {don_life_score}")

        time.sleep(0.8)

    else:
        type_text(f"\n🏆 Congratulations, {user_name}! You survived all {max_attempts} rounds!", 0.04)
        game_history.append(f"{user_name} survived all {max_attempts} rounds with a final score of {don_life_score}")

    # =============================
    # 🧾 Game Summary
    # =============================
    end_time = datetime.datetime.now()
    duration = (end_time - start_time).seconds

    slow_print("\n=== GAME OVER ===", 0.6)
    type_text(f"Player: {user_name}", 0.03)
    type_text(f"Final Life Score: {don_life_score}", 0.03)
    type_text(f"Total Rounds Survived: {round_num}", 0.03)
    type_text(f"🕒 Duration: {duration} seconds", 0.03)

    # Save game history
    save_game_history(user_name, game_history)


# =============================
# 🚀 Run Game
# =============================
if __name__ == "__main__":
    play_game()
