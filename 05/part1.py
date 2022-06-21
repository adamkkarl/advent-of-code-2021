#!/bin/python3

"""
Advent of Code 2021
Day 5 Part 1
https://adventofcode.com/2021/day/4
"""

__author__ = "Adam Karl"

INPUT_FILE = 'hydrothermalVents.txt'

def findOverlappingVents():
    """Draw all the vertical and horizontal vents on a grid then
    determine the number of overlapping points"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    # fill in horizontal and vertical lines
    for line in input:
        coords = line.split(' -> ')
        x1,y1 = list(map(int, coords[0].split(',')))
        x2,y2 = list(map(int, coords[1].split(',')))
        
        if x1 == x2:
            for j in range(min(y1,y2), max(y1,y2)+1):
                grid[x1][j] += 1
        elif y1 == y2:
            for i in range(min(x1,x2), max(x1,x2)+1):
                grid[i][y1] += 1
        
    
    # count overlap points
    overlaps = 0
    for i in range(1000):
        for j in range(1000):
            if grid[i][j] > 1:
                overlaps += 1
    return overlaps
    
def main():    
    overlaps = findOverlappingVents()
    print(f"Number of overlaps: {overlaps}")

if __name__ == "__main__":
    main()
