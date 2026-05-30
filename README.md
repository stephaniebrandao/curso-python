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

-----

# 💰 ATM Simulation

A simple, interactive command-line Python script that simulates the core functionality of an Automated Teller Machine (ATM). The user starts with a predefined balance and can perform multiple withdrawals until they choose to exit or their balance hits zero.

## 🚀 Features

- **Initial Balance:** Starts with a fixed balance of `500€`.
- **Input Validation:**
  - Rejects negative withdrawal amounts.
  - Rejects withdrawal requests that exceed the available balance.
  - Requires integer values for withdrawals.
- **Dynamic Control Flow:** Keeps processing transactions using a `while` loop until the user types `0` to quit or completely drains the account.

## 🛠️ How the Logic Works

The application runs a continuous loop that checks the user's available funds and processes inputs based on four specific states:

1. **Exit Trigger:** If the input is `0`, the loop terminates immediately via a `break` statement.
2. **Negative Value Guard:** If the input is less than `0`, it alerts the user and refuses the transaction.
3. **Overdraft Protection:** If the input exceeds the current balance, it notifies the user of insufficient funds.
4. **Successful Transaction:** If all guards pass, the requested amount is deducted from the balance, and the new total is displayed.

## 📦 How to Run

1. Make sure you have Python 3 installed on your system.
2. Save the code into a file named `projeto_python_2.py`.
3. Open your terminal or command prompt, navigate to the folder where the file is saved, and execute:
   
   ```bash
   python3 projeto_python_2.py
