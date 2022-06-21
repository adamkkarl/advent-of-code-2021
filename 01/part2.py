#!/bin/python3

"""
Advent of Code 2021
Day 1 Part 2
https://adventofcode.com/2021/day/1
"""

__author__ = "Adam Karl"

INPUT_FILE = 'input.txt'

def SonarSweep():
    """Parses and input file of depths and count the number of times a sliding window 
    of 3 depth measurements increases from the previous sliding window"""
    input = list()
    
    #parse input file as integer list
    with open(INPUT_FILE) as file:
        input = [int(line) for line in file]
    file.close()
    
    increases = 0
    depth1 = 0
    depth2 = 0
    depth3 = 0
    for i in range(3, len(input)):
        if input[i] > input[i-3]:
            increases += 1
    
    return increases
    
def main():    
    print("How many times does the depth sliding window increase?")
    increases = SonarSweep()
    print(f"Answer: {increases} times")

if __name__ == "__main__":
    main()
