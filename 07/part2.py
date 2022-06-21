#!/bin/python3

"""
Advent of Code 2021
Day 7 Part 2
https://adventofcode.com/2021/day/7
"""

__author__ = "Adam Karl"

INPUT_FILE = 'crabPositions.txt'

def alignCrabs():
    """Determine the position that requires the least amount of fuel for all
    crabs to reach. Return that position and the total fuel required"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    positions = list(map(int, input[0].split(',')))
    
    bestPos = -1
    minFuel = -1
    for x in range(min(positions), max(positions)+1):
        totalFuel = 0
        for p in positions:
            # subsequent steps take extra fuel
            for step in range(abs(p-x)):
                totalFuel += (step+1)
        
        if totalFuel < minFuel or minFuel == -1:
            bestPos = x 
            minFuel = totalFuel
        print(f"checked position {x}", flush=True)
    return bestPos, minFuel
    
def main():    
    pos, fuel = alignCrabs()
    print(f"Final position: {pos}")
    print(f"Total fuel required: {fuel}")

if __name__ == "__main__":
    main()
