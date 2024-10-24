#
#       project: whileLoops.py
#       author:  Ethan Gonzalez egonzalez2705003@woonsocketschools.com
#       author: Bryce Ishler bishler2709327@woonsocketschools.com
#       author: Ariel Medina amedina2718050@woonsocketschools.com
#       date written: 10/11/2024
#       Description: Bull and cow game

#       The first player, the gatekeeper, will secretly choose a three digit number with number 0 through 9 and no duplicates

#       The second player, the keymaster, will then get 10 guesses to try to guess the secret numbers

#       After each guess, the gatekeeper scores each guess with Bagels, Bulls, or Cows
#       Bagels means none of the digits in your guess are in the secret code.
#       Bull means one digit in your guess is correct and in the correct position of the secret code.
#       If you have three Bulls, you win and may lead a victory dance of one lap about the room!
#       Cow means one digit of your guess is present in the secret code, but in the wrong position.
#       If you get three Cows, your guess has all the correct digits, but all in the wrong place!

from getpass import getpass

# directions of the game
print('''"The first player is the Gatekeeper. They secretly choose a three digit number using the numbers zero to 9 with no duplicates. The second player, the Keymaster, gets 10 tries to guess the secret number. 
After each guess, the Gatekeeper “scores” using the following code:''')
print("")
print('''Bagels:     None of the digits in your guess are in the secret code.
Bull:   One digit in your guess is correct and in the correct position of the secret code. Please note that if you have three Bulls, you win and may lead a victory dance of one lap about the room!
Cow:    One digit of your guess is present in the secret code, but in the wrong position. If you get three Cows, your guess has all the correct digits, but all in the wrong place!
''')

# Keymaster will choose 3 digit number

print("Let's play Bulls and Cows")

Gatekeeper = input("Gatemaster, please select a three digit number with no duplicates: ")
Keymaster = input("Keymaster, guess a three digit number with no duplicates: ")
playing = True
while playing:
    bulls = 0
    cows = 0

    # Check each digit manually
    if Gatekeeper[0] == Keymaster[0]:
        bulls += 1
    elif Keymaster[0] in Gatekeeper:
        cows += 1

    if Gatekeeper[1] == Keymaster[1]:
        bulls += 1
    elif Keymaster[1] in Gatekeeper:
        cows += 1

    if Gatekeeper[2] == Keymaster[2]:
        bulls += 1
    elif Keymaster[2] in Gatekeeper:
        cows += 1

    if bulls == 3:
        print(f"You have {bulls} bulls, YOU WIN!")
        playing = False
    else:
        print(f"You have {bulls} bulls and {cows} cows")

    # Prompt for a new guess or end condition

    # This input Statement overwrites the Keymaster Code
    Keymaster = input("Keymaster, guess again: ")

    # Review notes from Linter
