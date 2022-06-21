#!/bin/python3

"""
Advent of Code 2021
Day 6 Part 1
https://adventofcode.com/2021/day/6
"""

__author__ = "Adam Karl"

INPUT_FILE = 'lanternfish.txt'

def simulatePopulation():
    """Given lanternfish ages, simulate the growth and population change
    in the fish over 80 days. Lanternfish give birth every 7 days"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    fish = list(map(int, input[0].split(',')))
    
    for _ in range(80):
        newFish = 0
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] < 0:
                # fish gives birth
                fish[i] = 6
                newFish += 1
        
        # add new fish after others have been decremented
        for i in range(newFish):
            fish.append(8)
    
    return len(fish)
    
def main():    
    numFish = simulatePopulation()
    print(f"Number of fish after 80 days: {numFish}")

if __name__ == "__main__":
    main()
