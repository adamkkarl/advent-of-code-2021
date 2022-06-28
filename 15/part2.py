#!/bin/python3

"""
Advent of Code 2021
Day 15 Part 2
https://adventofcode.com/2021/day/15
"""

__author__ = "Adam Karl"

INPUT_FILE = 'chitonDensity.txt'

def incrementGrid(grid, increment):
    """Given a grid, increment every element by the given increment. 
    Elements do not exceed 9 but instead wrap back around to 0"""
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = (grid[i][j] + increment) % 10
    return grid

def extendGridRight(gridA, gridB):
    """Given 2 grids with the same number of rows, 
    extend grid a to the right by adding grid b"""
    
    for i in range(len(gridA)):
        gridA[i] = gridA[i] + gridB[i]
    return gridA

def findLowestRiskPath():
    """Read in an int grid, find the path from the top left to the bottom right
    that incurs the lowest sum over its path.
    This time, the grid repeats 25 times in a 5x5 grid, with each space having
    a risk level increase the farther away from the original grid"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    grid = list()
    # build integer grid
    for i in range(len(input)):
        grid.append(list(map(int, input[i].strip())))

    gridTemplate = grid() # set template to input grid
    # extend to the right
    for i in range(1, 5):
        extendGridRight(grid, incrementGrid(gridTemplate.copy(), i))
        
    gridTemplate = grid.copy() # change template to wide grid slice
    # extend down
    for i in range(1, 5):
        grid = grid + incrementGrid(gridTemplate.copy(), i)
        
    print(len(grid))
    print(len(grid[0]))
        
    # don't count top left risk factor
    grid[0][0] = 0
    
    # work backwards to calculate the minimum risk path
    for i in range(len(grid))[::-1]:
        for j in range(len(grid[0]))[::-1]:
            if i < len(grid)-1 and j < len(grid[0])-1:
                # compare right and down
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
            elif i < len(grid)-1:
                # compare down
                grid[i][j] += grid[i+1][j]
            elif j < len(grid[0])-1:
                # compare to the right
                grid[i][j] += grid[i][j+1]    
                
    return grid[0][0]

def main():    
    risk = findLowestRiskPath()
    print(f"The path with the lowest total has a risk of {risk}")

if __name__ == "__main__":
    main()