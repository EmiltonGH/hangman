import random

word_list = ["Apple", "Orange", "Bananna", "Pears", "Strawberry"]
word = random.choice(word_list).lower()
print(word)


def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good Guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")


def ask_for_input():
    while True:
        guess = input("Guess a letter : ".lower())
        if guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character")

    check_guess(guess)


ask_for_input()
