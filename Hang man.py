import pyttsx3 as audio

speak = audio.init()
speak.say("Welcome to Hangman Game")
speak.runAndWait()

speak.say("Are you Ready to play the game ")
speak.runAndWait()

print("Welcome to HANGMAN ")

print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

import random

word = "Hangman"

allowed_guesses = 8
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    guess = input(f"Allowed errors left {allowed_guesses},Next guess: ")
    guesses.append(guess.lower())

    if guess.lower() not in word.lower():
        allowed_guesses -= 1
        if allowed_guesses == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You fouind the word ! it was {word}!")
else:
    print(f"Game Over ! The word was {word}")

print()

print("Thank you for playing hangman")

