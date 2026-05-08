# 🎯 Mini Project Challenge: Number Guessing Game (with levels)

# You’ll build a game where:

# computer picks a random number
# player tries to guess it
# you give hints (too high / too low)
# track attempts


import random



print("\n =====You are playing gussing game====== ")
def game():
    print("\n please select the level....")
    print(" 1. Easy mode 😋 (10 Attempts)")
    print(" 2. Normal mode 👍(7 Attempts)")
    print (" 3. Hard mode 💀 (only 5 Attempts)")
    
    level = input("> ")

    if (level == "1"):
        attempts = 10
    elif ( level == "2"):
        attempts = 7
    elif ( level == "3"):
        attempts = 5
    else :
        print("Invalid Input >>> Entering deafult Easy mode 😋")
        attempts = 10
    total_attempts = attempts
    computer_choice = random.randint(1,100)

    while attempts > 0 :
        print(f"\n You have {attempts} number of attemps all the best 👍")
        try :
            user_choice = int(input("please guess the number > "))
        except :
            print("Invalid input.. Please enter a number >>>>")
            continue
        if (user_choice == computer_choice) :
            used_attemps = total_attempts - attempts +1
            print(f"You have guessed it right, the number is {computer_choice}")
            print(f"\n You have guessed the number in {used_attemps} attempts.. Congratulation 🎉👏")
            return
        elif (user_choice > computer_choice):
            print("Please keep guessing lower number")
        elif (user_choice < computer_choice):
            print("Higher the number and keep guessing ")
        attempts -= 1
        if attempts == 0 :
            print(f"\n You lost the game 👾 . \n  The number was {computer_choice} \n Thanks for playing ... ")
while True:
    game()

    again= input("\nPlay again? (y/n): ").lower()
    if again == "n":
        print("Thanks for playing! 👋")
        break
    
