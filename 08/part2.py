#!/bin/python3

"""
Advent of Code 2021
Day 8 Part 2
https://adventofcode.com/2021/day/8
"""

__author__ = "Adam Karl"

INPUT_FILE = 'displayInput.txt'

def sortLetters(s):
    """Given a string of letters, return a string of those letters 
    sorted in alphabetical order"""
    sortedChars = sorted(s)
    return ''.join(sortedChars)

def containsAllCharacters(a, b):
    """Determine if string a contains ALL characters from string b"""
    for c in b:
        found = False 
        for ch in a:
            if ch == c:
                found = True 
        if found == False:
            return False 
    return True

def analyzeDisplays():
    """Given the 7-segment display data, 
    determine how many times 1, 4, 7, or 8 appear"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    sum = 0
    for line in input:
        
        # NOTE: patterns[10] will be the '|' delimiter
        patterns = [sortLetters(s.strip()) for s in line.split(' ')]
        
        # break apart into test cases and output, skipping delimiter
        testPatterns = patterns[:10]
        outputPatterns = patterns[11:]
        
        digitPatterns = ['' for _ in range(10)]
        
        # determine pattern of 1
        for p in testPatterns:
            if len(p) == 2:
                digitPatterns[1] = p
                break
                
        # determine pattern of 4
        for p in testPatterns:
            if len(p) == 4:
                digitPatterns[4] = p
                break
                
        # determine pattern of 7
        for p in testPatterns:
            if len(p) == 3:
                digitPatterns[7] = p
                break
                
        # determine pattern of 8
        for p in testPatterns:
            if len(p) == 7:
                digitPatterns[8] = p
                break
        
        # determine 3, 0, 6, 9
        # 2 and 5 still ambiguous until we know 9
        other = []       # will contain patterns for 2 and 5  
        for p in testPatterns:
            if len(p) == 5:
                # could be 2, 3, or 5
                if containsAllCharacters(p, digitPatterns[1]) == True:
                    # contains all segments from 1 -> 3
                    digitPatterns[3] = p
                else:
                    # cannot determine 2 from 5 yet
                    other.append(p)
            
            elif len(p) == 6:
                # could be 0, 6, or 9
                if containsAllCharacters(p, digitPatterns[4]) == True:
                    # contains all segments from 4 -> 9
                    digitPatterns[9] = p
                
                elif containsAllCharacters(p, digitPatterns[1]) == False:
                    # not 9 but doesn't have all segments from 1 -> 6
                    digitPatterns[6] = p
                else:
                    # 0 by default
                    digitPatterns[0] = p
        
        # since we know 9, we can differentiate 2 from 5 now
        for p in other:
            if containsAllCharacters(digitPatterns[9], p) == True:
                # contained in 9 means it's a 5
                digitPatterns[5] = p
            else:
                digitPatterns[2] = p
        
        value = 0
        # now we know the patterns of all digits and can calculate the output
        for i in range(4):
            digit = digitPatterns.index(outputPatterns[i])
            value += digit * 10**(3-i)
        sum += value
        
        print(digitPatterns)
        print(outputPatterns)
        print(value)
        print()
            
    return sum
    
def main():    
    n = analyzeDisplays()
    print(f"Sum of outputs: {n}")

if __name__ == "__main__":
    main()
