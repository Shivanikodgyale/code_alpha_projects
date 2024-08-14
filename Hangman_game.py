import random

# List of words for the game
WORDS = ['apple', 'banana', 'mango', 'strawberry', 'grapefruit', 'peach', 'blueberry', 'raspberry', 'kiwi', 'pomegranate']

# Choose a random word from the list
word_to_guess = random.choice(WORDS)

# Initialize variables for the game
guessed_letters = []
attempts_left = 6
game_over = False

# Game loop
while not game_over:
    # Print the current state of the game
    print('Attempts left:', attempts_left)
    print('Guessed letters:', ' '.join(guessed_letters))
    display = ''
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    print(display)

    # Get a guess from the user
    guess = input('Guess a letter: ').lower()

    # Check if the guess is valid
    if len(guess) != 1:
        print('Please enter only one letter.')
    elif guess in guessed_letters:
        print('You have already guessed this letter.')
    elif guess not in 'abcdefghijklmnopqrstuvwxyz':
        print('Please enter a letter from the alphabet.')
    else:
        # Add the guess to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in word_to_guess:
            print('Correct guess!')
        else:
            print('Incorrect guess.')
            attempts_left -= 1

        # Check if the player has won or lost
        if '_' not in display:
            print('Congratulations! You have won the game!')
            game_over = True
        elif attempts_left == 0:
            print('Sorry, you have run out of attempts. The word was:', word_to_guess)
            game_over = True