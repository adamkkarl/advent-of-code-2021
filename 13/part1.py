#!/bin/python3

"""
Advent of Code 2021
Day 13 Part 1
https://adventofcode.com/2021/day/13
"""

__author__ = "Adam Karl"

INPUT_FILE = 'thermalImaging.txt'

def fold(grid, axis, value):
    """given the grid and axis of the fold,
    return a folded grid along that axis"""
    print(f"Folding along {axis}={value}")
    
    # determine size of output grid
    maxX = len(grid[0])
    maxY = len(grid)
    if axis == 'x':
        maxX = value
    elif axis == 'y':
        maxY = value
    else:
        print(f"ERROR: {axis} is not a valid axis")
    
    ret = [[False for _ in range(maxX)] for _ in range(maxY)]
    print(f'Matrix: {len(ret[0])} by {len(ret)}\n')
    for y in range(len(ret)):
        for x in range(len(ret[0])):
            if grid[y][x] == True:
                ret[y][x] = True 
            if axis == 'x' and grid[y][len(grid[0])-x-1] == True:
                # check other side of x-axis fold
                ret[y][x] = True 
            elif axis == 'y' and grid[len(grid)-y-1][x] == True:
                # check other side of y-axis fold
                ret[y][x] = True 
    return ret

def origamiFold():
    """read in the bitmap of dots and execute one fold.
    then return the number of dots after one fold of the bitmap.
    Keep in mind that for this problem the x-axis is vertical"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    # clean input
    for i in range(len(input)):
        input[i] = input[i].strip()
    
    # extract coordinate data
    coords = []
    breakPoint = input.index('') #coords before this point, instructions after
    for i in range(breakPoint):
        coords.append(list(map(int, input[i].split(','))))
    
    # extract instructions
    instructions = []
    for i in range(breakPoint+1, len(input)):
        instruction = input[i].split(' ')
        axis, val = instruction[2].split('=')
        instructions.append([axis, int(val)])
    
    # determine grid size and add dots
    maxX = 0
    maxY = 0
    for c in coords:
        if c[0] > maxX:
            maxX = c[0]
        if c[1] > maxY:
            maxY = c[1]
    
    # build grid
    grid = [[False for _ in range(maxX+1)] for _ in range(maxY+1)]
    for coord in coords:
        x = coord[0]
        y = coord[1]
        grid[y][x] = True
        
    
    
    # count number of dots remaining
    dots = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == True:
                dots += 1
    print(f'Matrix: {maxX} x {maxY} with {dots} dots\n')
        
    # execute first fold
    axis = instructions[0][0]
    val = instructions[0][1]
    grid = fold(grid, axis, val)
    
    # count number of dots remaining
    dots = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == True:
                dots += 1
                
    # print(f'Matrix: {len(grid[0])} x {len(grid)} with {dots} dots after one fold\n')

    return dots

def main():    
    dots = origamiFold()
    print(f"There are {dots} dots after one fold")

if __name__ == "__main__":
    main()