import random

# List of words
words = ["apple", "banana", "grape", "orange", "mango"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_incorrect:

    # Display current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    # Check if player won
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
        break

    # Take input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        print("Wrong guess!")
        incorrect_guesses += 1

# If player loses
if incorrect_guesses == max_incorrect:
    print("\nGame Over!")
    print("The word was:", word)