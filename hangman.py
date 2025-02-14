import random

def get_random_word():
    words = ['python', 'hangman', 'computer', 'programming', 'development', 'function']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman_game():
    print("Welcome to Hangman!")
    word = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Guess the word:")
    while incorrect_guesses < max_incorrect_guesses:
        print(display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} attempts left.")
        else:
            print(f"Good guess! '{guess}' is in the word.")

        if set(word) == set(guessed_letters):
            print(f"Congratulations! You've guessed the word '{word}' correctly!")
            break
    else:
        print(f"Game Over! The word was '{word}'.")

# Start the game
hangman_game()
