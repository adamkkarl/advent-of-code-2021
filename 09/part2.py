#!/bin/python3

"""
Advent of Code 2021
Day 9 Part 2
https://adventofcode.com/2021/day/9
"""

__author__ = "Adam Karl"

INPUT_FILE = 'heightMap.txt'

def determineLargestBasins():
    """Determine the points of the heightmap that are lower than all
    adjacent points. Return the total risk levels of those points"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    grid = list()
    for line in input:
        grid.append(list(map(int, list(line.strip()))))
        
        
    largestBasins = [0,0,0]    
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
                #calculate size of surrounding basin
                points = [str(i) + ',' + str(j)]
                
                # append (new) higher adjacent points until no more can be found
                index = 0
                while index < len(points):
                    x, y = list(map(int, points[index].split(',')))
                    
                    if x > 0 and height < grid[x-1][y] and grid[x-1][y] != 9:
                        myPoint = str(x-1) + ',' + str(y)
                        if myPoint not in points:
                            points.append(myPoint)
                    if x < len(grid)-1 and height < grid[x+1][y] and grid[x+1][y] != 9:
                        myPoint = str(x+1) + ',' + str(y)
                        if myPoint not in points:
                            points.append(myPoint)
                    if y > 0 and height < grid[x][y-1] and grid[x][y-1] != 9:
                        myPoint = str(x) + ',' + str(y-1)
                        if myPoint not in points:
                            points.append(myPoint)
                    if y < len(grid)-1 and height < grid[x][y+1] and grid[x][y+1] != 9:
                        myPoint = str(x) + ',' + str(y+1)
                        if myPoint not in points:
                            points.append(myPoint)
                            
                    index += 1
    
                size = len(points)
                if size > min(largestBasins):
                    minIndex = largestBasins.index(min(largestBasins))
                    largestBasins[minIndex] = size
                
    return largestBasins

def main():    
    basins = determineLargestBasins() 
    print(f"Basins {basins[0]} x {basins[1]} x {basins[2]} = {basins[0]*basins[1]*basins[2]}")   

if __name__ == "__main__":
    main()