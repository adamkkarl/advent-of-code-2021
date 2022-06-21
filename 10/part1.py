#!/bin/python3

"""
Advent of Code 2021
Day 10 Part 1
https://adventofcode.com/2021/day/10
"""

__author__ = "Adam Karl"

INPUT_FILE = 'navigation.txt'

def findSyntaxCharacters():
    """Given a navigation file, on each line determine the first character to 
    incorrectly close a ( [ { or < and return the offending characters"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    incorrectChars = {')':0, ']':0, '}':0, '>':0}
    for myLine in input:
        line = list(myLine.strip())
        stack = []
        for  c in line:
            if c in ['(', '[', '{', '<']:
                stack.append(c)
            else:
                if c == ')' and stack.pop() != '(':
                    incorrectChars[c] += 1
                elif c == ']' and stack.pop() != '[':
                    incorrectChars[c] += 1
                elif c == '}' and stack.pop() != '{':
                    incorrectChars[c] += 1
                elif c == '>' and stack.pop() != '<':
                    incorrectChars[c] += 1
    return incorrectChars      

def main():    
    chars = findSyntaxCharacters() 
    print(f"{chars[')']}, {chars[']']}, {chars['}']}, {chars['>']}") 
    print(f"Total syntax score = {chars[')']*3 + chars[']']*57 + chars['}']*1197 + chars['>']*25137}")  

if __name__ == "__main__":
    main()