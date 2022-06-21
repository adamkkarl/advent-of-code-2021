#!/bin/python3

"""
Advent of Code 2021
Day 3 Part 2
https://adventofcode.com/2021/day/3
"""

__author__ = "Adam Karl"

INPUT_FILE = 'input.txt'

def binaryDiagnostic():
    """Use the binary numbers in your diagnostic report to calculate the 
    oxygen generator and CO2 scrubber ratings"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    oxygenList = input.copy()
    for pos in range(len(input[0])):
        if len(oxygenList) > 1:
            zeros = 0
            ones = 0
            # count frequency of bit 
            for line in oxygenList:
                if line[pos] == '0':
                    zeros += 1
                elif line[pos] == '1':
                    ones += 1
            
            mode = '0'
            if ones >= zeros:
                mode = '1'
            
            # filter out list based on the most common bit at that pos
            myList = list()
            for e in oxygenList:
                if e[pos] == mode:
                    myList.append(e)
                    
            oxygenList = myList.copy()
            
    co2List = input.copy()
    for pos in range(len(input[0])):
        if len(co2List) > 1:
            zeros = 0
            ones = 0
            # count frequency of bit 
            for line in co2List:
                if line[pos] == '0':
                    zeros += 1
                elif line[pos] == '1':
                    ones += 1
            
            mode = '0'
            if ones >= zeros:
                mode = '1'
            
            # filter out list based on the least common bit at that pos
            myList = list()
            for e in co2List:
                if e[pos] != mode:
                    myList.append(e)
                    
            co2List = myList.copy()
    
    return int(oxygenList[0], 2), int(co2List[0], 2)
    
def main():    
    oxy, co2 = binaryDiagnostic()
    print(f"oxygen generator rating: {oxy}")
    print(f"CO2 scrubber rating: {co2}")
    print(f"life support rating (oxy x co2): {oxy*co2}")

if __name__ == "__main__":
    main()
