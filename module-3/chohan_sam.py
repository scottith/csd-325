# Scott Macioce
# Module 3.2 Assignment
# 03/30/2025
# This program takes the cohan.py dice game with added changes based on module 3.2 requirements which
# have been annotated.


"""Cho-Han, by Al Sweigart al@inventwithpython.com
Modified by SAM
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

Bonus Rule: If the total of the dice is 2 or 7, you receive a 10 mon bonus!  # <-- ADDED: Bonus rule in game intro
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('sam: ')  # <-- CHANGED: Prompt now uses my initials 'sam:'
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2  # <-- ADDED: Store total of dice for bonus check

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input('sam: ').upper()  # <-- CHANGED: Prompt now uses initials 'sam:'
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Bonus condition:
    if total == 2 or total == 7:  # <-- ADDED: Bonus if dice total is 2 or 7
        print(f'You rolled a total of {total}! You get a 10 mon bonus!')
        purse += 10  # <-- ADDED: Add 10 mon bonus to purse

    # Determine if the player won:
    rollIsEven = (total) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot
        house_fee = pot * 12 // 100  # <-- CHANGED: House takes 12% instead of 10%
        print('The house collects a', house_fee, 'mon fee.')
        purse = purse - house_fee
    else:
        purse = purse - pot
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
