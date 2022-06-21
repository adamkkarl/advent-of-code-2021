#!/bin/python3

"""
Advent of Code 2021
Day 8 Part 1
https://adventofcode.com/2021/day/8
"""

__author__ = "Adam Karl"

INPUT_FILE = 'displayInput.txt'

def analyzeDisplays():
    """Given the 7-segment display data, 
    determine how many times 1, 4, 7, or 8 appear"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    ones = fours = sevens = eights = 0    
    for line in input:
        
        # NOTE: patterns[10] will be the '|' delimiter
        patterns = [s.strip() for s in line.split(' ')]
        
        for p in patterns[11:]:
            if len(p) == 2:
                # 2 segments can only display a 1
                ones += 1
            elif len(p) == 4:
                # 4 segments can only display a 4
                fours += 1
            elif len(p) == 3:
                # 3 segments can only display a 7
                sevens += 1
            elif len(p) == 7:
                # 7 segments can only display an 8
                eights += 1
    
    return ones, fours, sevens, eights
    
def main():    
    ones, fours, sevens, eights = analyzeDisplays()
    print(f"{ones} 1s, {fours} 4s, {sevens} 7s, {eights} 8s")
    print(f"Total: {ones + fours + sevens + eights}")

if __name__ == "__main__":
    main()
