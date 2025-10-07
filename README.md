# 🧨 Don_Destroyer

**Don_Destroyer** is a Python-based **number battle game** where you face off against an enemy named **DON**.
Your mission: **Survive all 20 rounds** by carefully selecting numbers that are **lower than DON’s life score**.
The challenge intensifies as you progress — with increasing difficulty and unpredictable outcomes.

---

## 🎮 Game Overview

* The player enters their **name** to begin the game.
* A random **life score** between `1` and `50` is assigned to **DON**.
* You’ll face **20 rounds**, each with different difficulty levels.
* Choose wisely — one wrong move, and it’s game over!

---

## ⚙️ Game Flow

### 1. User Input & Game Start

* The game prompts the player for their **name**.
* A random **life score** (`1–50`) is generated for DON.

### 2. Game Loop & Number Selection

The player must survive **20 attempts**.
Each round displays **5 random numbers**, depending on the difficulty range:

| Attempt Range | Number Range   | Difficulty |
| ------------- | -------------- | ---------- |
| 1–5           | 15 – 100       | 🟢 Easy    |
| 6–10          | 250 – 2000     | 🟡 Medium  |
| 11–15         | 3000 – 10000   | 🟠 Hard    |
| 16–20         | 20000 – 100000 | 🔴 Extreme |

---

## 🧩 Game Rules

1. If the chosen number **is not** in the displayed list → ❌ *You lose!*
2. If the chosen number is **higher** than DON’s life score → 💀 *You lose!*
3. If the chosen number is **lower**, it gets **added** to DON’s life score → ✅ *Continue!*
4. Survive **all 20 attempts** → 🏆 *You win the game!*

---

## 📝 Game History & File Handling

* Every action and outcome is logged in a **game history list**.
* Once the game ends (win or lose), the history is **saved** to a `.txt` file.
* The filename includes a **unique timestamp** for easy reference (e.g., `game_history_2025-10-07_14-30-55.txt`).

---

## 💻 Technologies Used

* **Python Standard Library** – Input/output handling and control flow
* **Random Module** – Generating DON’s life score and round numbers
* **Datetime Module** – Creating unique filenames for history files
* **File Handling** – Writing detailed game logs for each session

---

## 🏁 How to Run

1. Clone or download this repository.
2. Run the Python file:

   ```bash
   python don_destroyer.py
   ```
3. Follow the on-screen instructions to play.
4. After the game ends, check your **game history file** in the project folder.

---

## 🧠 Example Outcome

```
Enter your name: Shibishan  
DON’s Life Score: 32  

Round 1 Numbers: [25, 67, 88, 91, 43]  
Choose your number: 25  
✅ You survived! DON’s life score is now 57  

...  

🎉 Congratulations, Shibishan! You survived all 20 rounds!
Game history saved as: game_history_2025-10-07_14-30-55.txt
```

---

## 📦 Future Enhancements

* Add a **GUI version** using Tkinter or PyGame
* Implement **scoreboards** to track top players
* Introduce **power-ups** or **special abilities**
* Add **sound effects** and **visual animations**

---

## 👨‍💻 Author

**Shibishan**
*BSc (Hons) Software Engineering Student*
University of Westminster | IIT Colombo
💼 GitHub: [Shibishan](https://github.com/Shibishan)
