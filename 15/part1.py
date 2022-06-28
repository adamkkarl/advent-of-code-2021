#!/bin/python3

"""
Advent of Code 2021
Day 15 Part 1
https://adventofcode.com/2021/day/15
"""

__author__ = "Adam Karl"

INPUT_FILE = 'chitonDensity.txt'


def findLowestRiskPath():
    """Read in an int grid, find the path from the top left to the bottom right
    that incurs the lowest sum over its path"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    grid = list()
    # build integer grid
    for i in range(len(input)):
        grid.append(list(map(int, input[i].strip())))
        
    # don't count top left risk factor
    grid[0][0] = 0
    
    # work backwards to calculate the minimum risk path
    for i in range(len(grid))[::-1]:
        for j in range(len(grid[0]))[::-1]:
            if i < len(grid)-1 and j < len(grid[0])-1:
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
            elif i < len(grid)-1:
                grid[i][j] += grid[i+1][j]
            elif j < len(grid[0])-1:
                grid[i][j] += grid[i][j+1]    
                
    return grid[0][0]
    

def main():    
    risk = findLowestRiskPath()
    print(f"The path with the lowest total has a risk of {risk}")

if __name__ == "__main__":
    main()