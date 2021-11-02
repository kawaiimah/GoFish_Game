# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:48:49 2020

Go Fish game against the computer

"""

import secrets
import sys
import time

def shuffle():
    
    # Create ordered deck
    deck = []
    for j in range(1,14):
        deck.append((j, 'H'))
    for j in range(1,14):
        deck.append((j, 'C'))
    for j in range(1,14):
        deck.append((j, 'D'))
    for j in range(1,14):
        deck.append((j, 'H'))
        
    # Pops a card from deck and inserts into a random position
    # in the shuffled deck being built
    shuffled = []
    for i in range(len(deck)):
        card = deck.pop()
        pos = secrets.randbelow(i+1)
        shuffled.insert(pos, card)
    
    return shuffled


def showcards(cards):
    
    # Construct cardstr to be printed
    cardstr = ''
    for i in range(len(cards)):
        
        card = cards[i]
        
        # add AJQK or numeral accordingly
        if card[0] == 1:
            cardstr += 'A'
        elif card[0] == 11:
            cardstr += 'J'
        elif card[0] == 12:
            cardstr += 'Q'
        elif card[0] == 13:
            cardstr += 'K'
        else:
            cardstr += str(card[0])
        
        # add suit accordingly
        if card[1] == 'S':
            cardstr += '♠, '
        if card[1] == 'H':
            cardstr += '♥, '
        if card[1] == 'D':
            cardstr += '♦, '
        if card[1] == 'C':
            cardstr += '♣, '
    
    print(cardstr)

def checksets(hand,sets):
    
    # Check for completed sets
    if hand != []:
        count = 0
        rank = 0
        for i in range(len(hand)-1,-1,-1):
            if rank != hand[i][0]:
                rank = hand[i][0]
                count = 1
            else:
                count += 1
            if count == 4:
                del hand[i:i+4]
                if rank == 1:
                    sets.append('A')
                elif rank == 11:
                    sets.append('J')
                elif rank == 12:
                    sets.append('Q')
                elif rank == 13:
                    sets.append('K')
                else:
                    sets.append(str(rank))
                count = 0
    return hand, sets

def main():
    
    print('\n---Go Fish Game---')
    
    # Shuffle and deal 7 cards each to comp and player
    shuffled = shuffle()
    cheat = False
    gamestate = 0 # 0=player turn, 1=comp turn, 2=end game
    comp = []
    player = []
    compsets = []
    playersets = []
    for i in range(7):
        comp.append(shuffled.pop())
        player.append(shuffled.pop())
    
    comp = sorted(comp, key=lambda tup: tup[0])
    player = sorted(player, key=lambda tup: tup[0])
    
    while True:
        
        # Check for completed sets
        comp,compsets = checksets(comp,compsets)
        player,playersets = checksets(player,playersets)
        if player == [] or comp == []:
            gamestate = 2
        
        # Print Board
        print('\nComputer completed sets:')
        print(compsets)
        print('Your completed sets:')
        print(playersets)
        
        print('Computer cards:')
        if cheat:
            showcards(comp)
        else:
            cardstr = ''
            for i in comp:
                cardstr += '▮▮, '
            print(cardstr)
        
        print('Your cards:')
        showcards(player)
        
        
        if gamestate == 0: # Player's turn
            
            # Get player input and check validity
            valid = False
            validlist = set()
            for card in player:
                validlist.add(card[0])
            while not valid:
                choice = input('Your turn (A, 2-10, J, Q, K or X to quit)? ').upper()
                if choice in ['A','J','Q','K','2','3','4','5','6','7','8','9','10','X','C']:
                    if choice == 'A':
                        choice = 1
                    elif choice == 'J':
                        choice = 11
                    elif choice == 'Q':
                        choice = 12
                    elif choice == 'K':
                        choice = 13
                    elif choice in ['2','3','4','5','6','7','8','9','10']:
                        choice = int(choice)
                    elif choice == 'X':
                        sys.exit()
                    else:
                        cheat = not cheat
                    if choice in validlist or choice == 'C':
                        valid = True
                    else:
                        print('You can only ask for cards you have!')
                else:
                    print('Invalid input, pls try again.')
                    
            # Check if player choice in comp
            # If yes, take card from comp and check if comp is empty
            # Otherwise draw from shuffled
            if choice == 'C':
                pass
            else:
                gamestate = 1
                for i in range(len(comp)-1,-1,-1):
                    if comp[i][0] == choice:
                        player.append(comp.pop(i))
                        player = sorted(player, key=lambda tup: tup[0])
                        gamestate = 0
                if gamestate == 0:
                    print('\nSuccess!\n')
                else:
                    print('\nComputer says: Go Fish!')
                    time.sleep(1)
                    if len(shuffled)>0:
                        print('Drawing card from stock...')
                        time.sleep(1)
                        card = shuffled.pop()
                        player.append(card)
                        player = sorted(player, key=lambda tup: tup[0])
                        rank = card[0]
                        if rank == 1:
                            rank = 'A'
                        elif rank == 11:
                            rank = 'J'
                        elif rank == 12:
                            rank = 'Q'
                        elif rank == 13:
                            rank = 'K'
                        else:
                            rank = str(rank)
                        # Check if drawn card matches choice
                        if card[0] == choice:
                            gamestate = 0
                            if choice == 1:
                                print('It is an A!\n')
                            else:
                                print('It is a ' + rank + '!\n')
                        else:
                            if rank == 'A':
                                print('You drew an A.\n')
                            else:
                                print('You drew a ' + rank + '.\n')
                    else:
                        print('There are no more cards to draw.\n')
                time.sleep(2)
        
        
        elif gamestate == 1: # Comp's turn           
            # Random choice weighted by number of cards
            print('\nComputer\'s turn...')
            time.sleep(2)
            choice = comp[secrets.randbelow(len(comp))][0]
            rank = ''
            if choice == 1:
                rank = 'A'
            elif choice == 11:
                rank = 'J'
            elif choice == 12:
                rank = 'Q'
            elif choice == 13:
                rank = 'K'
            else:
                rank = str(choice)
            print('Computer asks for ' + rank + '...')
            time.sleep(2)
            # Check if comp choice in player
            # If yes, take card from player and check if player is empty
            # Otherwise draw from shuffled
            gamestate = 0
            for i in range(len(player)-1,-1,-1):
                if player[i][0] == choice:
                    comp.append(player.pop(i))
                    comp = sorted(comp, key=lambda tup: tup[0])
                    gamestate = 1
            if gamestate == 1:
                print('Success!\n')
            else:
                print('\nYou say: Go Fish!')
                time.sleep(1)
                if len(shuffled)>0:
                    print('Computer is drawing card from stock...')
                    time.sleep(1)
                    card = shuffled.pop()
                    comp.append(card)
                    comp = sorted(comp, key=lambda tup: tup[0])
                    rank = card[0]
                    if rank == 1:
                        rank = 'A'
                    elif rank == 11:
                        rank = 'J'
                    elif rank == 12:
                        rank = 'Q'
                    elif rank == 13:
                        rank = 'K'
                    else:
                        rank = str(rank)
                    # Check if drawn card matches choice
                    if card[0] == choice:
                        gamestate = 1
                        if choice == 1:
                            print('It is an A!\n')
                        else:
                            print('It is a ' + rank + '!\n')
                    else:
                        print('It did not match Computer\'s choice.\n')
                else:
                    print('There are no more cards to draw.\n')
            time.sleep(1)
            
        
        else: # End game
            print('\nGame over!')
            if len(compsets) > len(playersets):
                print('Computer wins!\n')
            elif len(compsets) < len(playersets):
                print('You win!!!\n')
            else:
                print('It is a tie!\n')
            return

while True:
    
    main()
    if input('Play again (y/n)? ').lower() == 'n':
        sys.exit()
