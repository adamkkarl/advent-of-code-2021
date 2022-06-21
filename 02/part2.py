#!/bin/python3

"""
Advent of Code 2021
Day 2 Part 2
https://adventofcode.com/2021/day/2
"""

__author__ = "Adam Karl"

INPUT_FILE = 'divingInstructions.txt'

def simulateMovement():
    """Simulates the horizontal position and depth based on an instruction file,
    then returns the final values"""
    horizontal = 0
    depth = 0
    aim = 0
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    for line in input:
        instruction = line.split()
        direction = instruction[0]
        distance = int(instruction[1])
        
        if direction == 'up':
            aim -= distance
        elif direction == 'down':
            aim += distance
        elif direction == 'forward':
            horizontal += distance 
            depth += (aim * distance)
        else:
            print(f"ERROR: direction {direction} not valid")
        
    
    return horizontal, depth
    
def main():    
    h, d = simulateMovement()
    print(f"Horizontal position: {h}")
    print(f"Depth: {d}")
    print(f"horizontal position x depth: {h*d}")

if __name__ == "__main__":
    main()
