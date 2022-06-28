#!/bin/python3

"""
Advent of Code 2021
Day 15 Part 2
https://adventofcode.com/2021/day/15
"""

__author__ = "Adam Karl"

INPUT_FILE = 'chitonDensity.txt'

class PrioQueue(object):
    def __init__(self):
        self.queue = list()
        
    def __str__(self):
        ret = ''
        for row, col, risk in self.queue:
            ret += f'({str(row)},{str(col)}) = {risk}\n'
        return ret
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, row, col, risk):
        """Insert in increasing order of risk"""
        i = 0
        while i < len(self.queue) and risk > self.queue[i][2]:
            i += 1
        self.queue.insert(i, [row, col, risk])
        
    def pop(self):
        ret = self.queue[0]
        del self.queue[0]
        return ret

def createLargeGrid(grid):
    """Given a grid, tile it 5x5 times with an increase in magnitude
    based on distance from origin"""
    rows = len(grid)
    cols = len(grid[0])
    ret = [[0 for _ in range(cols * 5)] for _ in range(rows * 5)]
    
    for i in range(len(ret)):
        for j in range(len(ret[0])):
            originalVal = grid[i % rows][j % cols]
            increment = i//rows + j//cols
            
            finalVal = originalVal
            for _ in range(increment):
                finalVal += 1
                if finalVal > 9:
                    finalVal = 1
            ret[i][j] = finalVal
    return ret

def findLowestRiskPath():
    """Read in an int grid, find the path from the top left to the bottom right
    that incurs the lowest sum over its path.
    This time, the grid repeats 25 times in a 5x5 grid, with each space having
    a risk level increase the farther away from the original grid"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    # read in integer grid
    originalGrid = list()
    for i in range(len(input)):
        originalGrid.append(list(map(int, input[i].strip())))
    
    # tile grid in a 5x5 based on given rules
    grid = createLargeGrid(originalGrid.copy())  
        
    # don't count top left risk factor
    grid[0][0] = 0
    
    # create grid to find best path from this position
    bestPathGrid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    bestPathGrid[-1][-1] = grid[-1][-1]
    
    pQueue = PrioQueue()
    pQueue.insert(len(grid)-1, len(grid[0])-1, grid[-1][-1])

    filledCells = 1
    while pQueue.isEmpty() == False:
        i, j, risk = pQueue.pop()
        
        if i < len(grid)-1 and bestPathGrid[i+1][j] == 0:
            # continue path down
            myRisk = risk + grid[i+1][j]
            bestPathGrid[i+1][j] = myRisk
            pQueue.insert(i+1, j, myRisk)
            filledCells += 1
        if i > 0 and bestPathGrid[i-1][j] == 0:
            # continue path up
            myRisk = risk + grid[i-1][j]
            bestPathGrid[i-1][j] = myRisk
            pQueue.insert(i-1, j, myRisk)
            filledCells += 1
        if j < len(grid)-1 and bestPathGrid[i][j+1] == 0:
            # continue path right
            myRisk = risk + grid[i][j+1]
            bestPathGrid[i][j+1] = myRisk
            pQueue.insert(i, j+1, myRisk)
            filledCells += 1
        if j > 0 and bestPathGrid[i][j-1] == 0:
            # continue path up
            myRisk = risk + grid[i][j-1]
            bestPathGrid[i][j-1] = myRisk
            pQueue.insert(i, j-1, myRisk)
            filledCells += 1
        print(f"{filledCells} / {len(grid)*len(grid[0])} complete", flush=True)
    
    return bestPathGrid[0][0]

def main():    
    risk = findLowestRiskPath()
    print(f"\nThe path with the lowest total has a risk of {risk}")

if __name__ == "__main__":
    main()