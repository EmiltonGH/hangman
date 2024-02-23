## Hangman Game

Hangman is a classic word-guessing game where the player attempts to guess a word by suggesting letters within a certain number of guesses. This Python script implements a simple version of the Hangman game.

## How to Play

Setup: Run the script using Python. Make sure you have Python installed on your system.

Game Start: Upon running the script, the game will randomly select a word from the provided word list.

Guessing: Enter a single alphabetical character as your guess. You have a limited number of lives to guess the word.
Win or Lose: If you correctly guess all the letters in the word before running out of lives, you win the game. If you run out of lives before guessing the word, you lose.

## Features

Random selection of words from a predefined list.
Limited number of lives for the player.
Validation of user input.
Feedback on the correctness of guesses.
End game messages for winning or losing.

## Usage
python hangman.py

To play the game, simply run the script in a Python environment. Follow the on-screen instructions to make guesses and play the game.Customization

You can customize the word list by modifying the word_list variable in the script.
Adjust the number of lives by changing the num_lives parameter in the Hangman class instantiation.

## Requirements

Python 3.x

## Suggestions for Improvement

Display the progress of guessed letters to the player.
Implement a graphical user interface for a more engaging experience.
Add difficulty levels with varying word lengths or lives.
Refactor the code for better modularity and readability.
