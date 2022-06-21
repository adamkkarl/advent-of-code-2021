#!/bin/python3

"""
Advent of Code 2021
Day 10 Part 2
https://adventofcode.com/2021/day/10
"""

__author__ = "Adam Karl"

INPUT_FILE = 'navigation.txt'

def medianSyntaxScore():
    """Given a navigation file, determine the syntax score of each line and
    return the median score"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    scores = list()
    for myLine in input:
        line = list(myLine.strip())
        
        corrupted = False
        stack = []
        for c in line:
            if c in ['(', '[', '{', '<']:
                stack.append(c)
            else:
                if c == ')' and stack.pop() != '(':
                    corrupted = True
                elif c == ']' and stack.pop() != '[':
                    corrupted = True
                elif c == '}' and stack.pop() != '{':
                    corrupted = True
                elif c == '>' and stack.pop() != '<':
                    corrupted = True
        
        if corrupted == False:
            closingStack = []
            appendStack = []
            for c in line[::-1]:
                if c in [')', ']', '}', '>']:
                    closingStack.append(c)
                else:
                    if closingStack and c == '(' and closingStack[-1] == ')':
                        closingStack.pop()
                    elif closingStack and c == '[' and closingStack[-1] == ']':
                        closingStack.pop()
                    elif closingStack and c == '{' and closingStack[-1] == '}':
                        closingStack.pop()
                    elif closingStack and c == '<' and closingStack[-1] == '>':
                        closingStack.pop()
                    else:
                        #didn't connect bracket, need to add char at end
                        if c == '(':
                            appendStack.append(')')
                        elif c == '[':
                            appendStack.append(']')
                        elif c == '{':
                            appendStack.append('}')
                        elif c == '<':
                            appendStack.append('>')
                        else:
                            print(f"ERROR: unexpected character {c} found")
                            
            score = 0
            # determine score from characters to be appended               
            for c in appendStack:
                score *= 5
            
                if c == ')':
                    score += 1
                elif c == ']':
                    score += 2
                elif c == '}':
                    score += 3 
                elif c == '>':
                    score += 4
                else:
                    print(closingStack)
                    print(f"ERROR: unexpected character {c} found")
                
            # print(line)
            # print(appendStack)
            # print("closing ", closingStack)
            # print(score)
            # print()
            scores.append(score)
        
    scores.sort()
    print(f"Scores: {scores}")
    print(len(scores))
    return scores[len(scores) // 2]

def main():    
    s = medianSyntaxScore() 
    print(f"Median syntax score: {s}") 

if __name__ == "__main__":
    main()