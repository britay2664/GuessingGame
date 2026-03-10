# Name: Brian Taylor
# Date: March 9, 2026
# Description: This program asks the user to guess a number between 1 and 10.
# It tells the user if the guess is too high, too low, or correct and counts
# the number of attempts. It then demonstrates both a while loop and a for loop
# that increment the correct guess value.

# Ask for user information
userName = input("Enter your name: ")
studentId = input("Enter your Student ID: ")

print("\n-----------------------------------")
print(f"Welcome BriTay2664!")
print("-----------------------------------\n")

# predetermined correct number
correctNumber = 5
guessCount = 0
userGuess = 0

# Guessing game
while userGuess != correctNumber:
    userGuess = int(input("Enter a number between 1 and 10: "))
    guessCount += 1

    if userGuess > correctNumber:
        print("Your guess is too high.\n")

    elif userGuess < correctNumber:
        print("Your guess is too low.\n")

    else:
        print("Congratulations! You guessed correctly.\n")

print(f"It took you {guessCount} tries to guess the correct number.\n")

# While loop that runs 5 times
print("Output from the while loop:")

counter = 0
while counter < 5:
    result = correctNumber + counter + 1
    print(f"{correctNumber} incremented by 1 is {result}")
    counter += 1

# For loop that does the same thing
print("\nOutput from the for loop:")

for counter in range(5):
    result = correctNumber + counter + 1
    print(f"{correctNumber} incremented by 1 is {result}")