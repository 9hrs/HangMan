

import random

# HANGMAN


def hangman():
    words = ['python', 'hangman', 'game', 'player', 'guess']
    word = random.choice(words)
    guess_letters = []
    attempts = 6

    while attempts > 0:
        for letter in word:
            if letter in guess_letters:
                print(letter,end=' ')
            else:
                print('_', end=' ')
        print()

        guess = input('guess a letter')
        if guess in word:
            print('correct guess!')
        else:
            print('incorrect guess')
            attempts -= 1


hangman()




