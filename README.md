# 🔢 Number Guessing Game

A simple, interactive terminal-based guessing game written in Python.
The program uses a predefined number and guides the player to the correct answer by providing real-time hints ("bigger" or "smaller").

## 🚀 Features

- **Interactive Loop:** The game runs continuously until the player guesses the correct number.
- **Dynamic Hints:** Gives instant feedback if your guess is too high or too low.
- **Input Validation (Bonus):** Built with clean, readable, and structured Python logic.

## 🛠️ How It Works

The game uses a `while` loop to check the user's input against a `secret_number`. 

1. The game prompts you to enter a number between 1 and 10.
2. If your guess is lower than the secret number, it outputs: `The secret number is bigger!`
3. If your guess is higher than the secret number, it outputs: `The secret number is smaller!`
4. Once you guess correctly, it congratulates you and terminates the loop.

## 📋 Prerequisites

To run this project, you only need Python installed on your machine:
- [Python 3.x](https://www.python.org/)

## 📦 Installation & Running the Game

1. **Clone the repository** (or just copy the script file):
   ```bash
   git clone [https://github.com/stephaniebrandao/curso-python.git](https://github.com/stephaniebrandao/curso-python.git)
   cd curso-python

2. **Run the script directly from your terminal:**
   ```bash
   python3 projeto_python.py
