#!/bin/python3

"""
Advent of Code 2021
Day 4 Part 1
https://adventofcode.com/2021/day/4
"""

__author__ = "Adam Karl"

INPUT_FILE = 'bingoInput.txt'

def sumUncalled(card, boolCard):
    """given a card and its boolean counterpart, sum up all the numbers on the 
    card that haven't been called"""
    sum = 0
    for r in range(5):
        for c in range(5):
            if boolCard[r][c] == False:
                sum += card[r][c] 
    return sum

def checkWin(card):
    """Given a 5x5 array of booleans corresponding to if that space has been called,
    determine if that card has a bingo"""
    #check rows
    for row in range(5):
        win = True
        for col in range(5):
            if card[row][col] == False:
                win = False 
        if win == True:
            return True
        
    #check cols
    for col in range(5):
        win = True
        for row in range(5):
            if card[row][col] == False:
                win = False 
        if win == True:
            return True
    
    #check '\' diagonal
    win = True
    for i in range(5):
        if card[i][i] == False:
            win = False
    if win == True:
            return True
        
    #check '/' diagonal
    win = True
    for i in range(5):
        if card[4-i][i] == False:
            win = False
    if win == True:
            return True
    
    return False

def simulateBingo():
    """Simulate a bingo game based on the input file and determine the
    score of the first winning bingo card"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    calledNumbers = list(map(int, input[0].split(',')))
    bingoCards = list()
    
    # parse input into list of cards
    i = 2   #where first bingo card starts
    while i < len(input):
        card = list()
        for _ in range(5):
            card.append(list(map(int, input[i].split())))
            i += 1
        bingoCards.append(card)
        i += 1 # skip over blank line
    
    winningTurn = -1
    winningScore = -1
    for card in bingoCards:
        boolCard = [[False for i in range(5)] for j in range(5)]
        for turn in range(len(calledNumbers)):
            n = calledNumbers[turn]
            for r in range(5):
                for c in range(5):
                    if card[r][c] == n:
                        boolCard[r][c] = True 
            if checkWin(boolCard) == True:
                score = calledNumbers[turn] * sumUncalled(card, boolCard)
                if turn > winningTurn:
                    winningScore = score 
                    winningTurn = turn 
                break
            
    return winningTurn, winningScore
    
def main():    
    turn, score = simulateBingo()
    print(f"Winning Turn: {turn}")
    print(f"Final Score: {score}")

if __name__ == "__main__":
    main()
