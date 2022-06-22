#!/bin/python3

"""
Advent of Code 2021
Day 11 Part 2
https://adventofcode.com/2021/day/11
"""

__author__ = "Adam Karl"

INPUT_FILE = 'octopusGrid.txt'

def isValidCoordinate(x, y, rows, cols):
    """Given a coordinate and dimensions of the grid, return True
    if the point is part of the grid"""
    if x < 0 or x > rows-1:
        return False 
    if y < 0 or y > cols-1:
        return False 
    return True

def simulateOctopi():
    """Simulates steps of energy levels of a grid of octopusi until all 
    octopi flash. Each octopus increases energy by 1 each turn. An octopus 
    flashes at energy 10+, increasing the energy of surrounding octopi.
    Return the step number when all octopi flash"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    # read file into grid
    grid = list()
    for line in input:
        parsedLine = list(line.strip())
        grid.append(list(map(int, parsedLine)))
    
    
    # simulate 100 steps and keep track of total flashes
    step = 0
    while True:      
        step += 1
        
        # increment each element of grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c] += 1
        
        # determine flashes
        foundFlash = True 
        while foundFlash:
            foundFlash = False
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] > 9:
                        foundFlash = True
                        # increase energy of surrounding spaces
                        for x in [r-1, r, r+1]:
                            for y in [c-1, c, c+1]:
                                if isValidCoordinate(x, y, len(grid), len(grid[0])) and grid[x][y] != -1:
                                    grid[x][y] += 1
                        # mark space as 'flashed' with a -1
                        grid[r][c] = -1
        
        numFlashes = 0
        # count up number of flashes and reset their energy to 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == -1:
                    numFlashes += 1
                    grid[r][c] = 0
        
        # if all octopi have flashed, return the step number
        if numFlashes == len(grid)*len(grid[0]):
            return step

def main():    
    step = simulateOctopi()
    print(f"The octopi synchronize flashes on step {step}")

if __name__ == "__main__":
    main()