import random

result = random.randint(1, 100)  # computer's secret number
attempts = 0
max_attempts = 6

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess > result:
        print("Your guess is high")
    elif guess < result:
        print("Your guess is low")
    else:
        print("Congratulations! Your guess is right.")
        break

if attempts == max_attempts and guess != result:
    print("Game over! You've used all attempts.")
