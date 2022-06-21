#!/bin/python3

"""
Advent of Code 2021
Day 3 Part 1
https://adventofcode.com/2021/day/3
"""

__author__ = "Adam Karl"

INPUT_FILE = 'input.txt'

def binaryDiagnostic():
    """Use the binary numbers in your diagnostic report to calculate the 
    gamma rate and epsilon rate, then multiply them together."""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    gamma = ''
    epsilon = ''
    for pos in range(len(input[0])):
        zeros = 0
        ones = 0
        for line in input:
            if line[pos] == '0':
                zeros += 1
            elif line[pos] == '1':
                ones += 1
        if zeros > ones:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        elif zeros < ones:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
    
    return int(gamma, 2), int(epsilon, 2)
    
def main():    
    g, e = binaryDiagnostic()
    print(f"Gamma rate: {g}")
    print(f"Epsilon rate: {e}")
    print(f"Power consumption (g x e): {g*e}")

if __name__ == "__main__":
    main()
