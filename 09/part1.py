#!/bin/python3

"""
Advent of Code 2021
Day 9 Part 1
https://adventofcode.com/2021/day/9
"""

__author__ = "Adam Karl"

INPUT_FILE = 'heightMap.txt'

def analyzeRisk():
    """Determine the points of the heightmap that are lower than all
    adjacent points. Return the total risk levels of those points"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    grid = list()
    for line in input:
        grid.append(list(map(int, list(line.strip()))))
    
    totalRisk = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            height = grid[i][j]
            isLowPoint = True
            if i > 0 and height >= grid[i-1][j]:
                isLowPoint = False 
            if i < len(grid)-1 and height >= grid[i+1][j]:
                isLowPoint = False 
            if j > 0 and height >= grid[i][j-1]:
                isLowPoint = False 
            if j < len(grid[0])-1 and height >= grid[i][j+1]:
                isLowPoint = False 
            if isLowPoint == True:
                totalRisk += height + 1
    return totalRisk 

def main():    
    risk = analyzeRisk() 
    print(f"Total risk = {risk}")   

if __name__ == "__main__":
    main()