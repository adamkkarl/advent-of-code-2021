#!/bin/python3

"""
Advent of Code 2021
Day 1 Part 1
https://adventofcode.com/2021/day/1
"""

__author__ = "Adam Karl"

INPUT_FILE = 'input.txt'

def SonarSweep():
    """Parses and input file of depths and count the number of times a depth 
    measurement increases from the previous measurement"""
    input = list()
    
    #parse input file as integer list
    with open(INPUT_FILE) as file:
        input = [int(line) for line in file]
    file.close()
    
    increases = 0
    lastDepth = -1
    for depth in input:
        if depth>lastDepth and lastDepth>0:
            increases += 1
        lastDepth = depth
    
    return increases
    
def main():    
    print("How many times does the depth increase?")
    increases = SonarSweep()
    print(f"Answer: {increases} times")

if __name__ == "__main__":
    main()
