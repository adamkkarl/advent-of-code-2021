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
    in the fish over 256 days. Lanternfish give birth every 7 days"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    fish = list(map(int, input[0].split(',')))
    
    fishAgeFreqTable = [0 for _ in range(9)]
    for age in fish:
        fishAgeFreqTable[age] += 1
    
    for day in range(256):
        givingBirth = fishAgeFreqTable[0]
        
        #decrement ages
        for i in range(0, 8):
            fishAgeFreqTable[i] = fishAgeFreqTable[i+1]
            
        #reset birth cycle and add babies
        fishAgeFreqTable[6] += givingBirth
        fishAgeFreqTable[8] = givingBirth
       
    # count total fish in freq table 
    totalFish = 0
    for n in fishAgeFreqTable:
        totalFish += n
    
    return totalFish
    
def main():    
    numFish = simulatePopulation()
    print(f"Number of fish after 256 days: {numFish}")

if __name__ == "__main__":
    main()
