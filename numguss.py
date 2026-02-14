import random

number = random.randint(1, 100)
score = 100
attempts = 0

print("🎯 Number Guessing Game with Score")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        score -= 10
        print("Too low!")
    elif guess > number:
        score -= 10
        print("Too high!")
    else:
        print("\n🎉 Congratulations!")
        print("Correct Number:", number)
        print("Attempts:", attempts)
        print("Final Score:", max(score, 0))
        break

    if score <= 0:
        print("\n❌ Game Over!")
        print("You've lost all your points.")
        print("The correct number was:", number)
        break
