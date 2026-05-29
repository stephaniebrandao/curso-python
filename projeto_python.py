# Guessing Game

# While playing, the user needs to guess a secret number.
# They can try as many times as they want until they guess the right one.


secret_number = 5
attempt = 0

while attempt != secret_number:
    attempt = int(input("Guess a number from 1 to 10: "))

    if attempt < secret_number:
        print("The secret number is bigger!")
    elif attempt > secret_number:
        print("The secret number is smaller!")
    else:
        print("Congrats! You nailed it!")
