#!/bin/python3

"""
Advent of Code 2021
Day 14 Part 1
https://adventofcode.com/2021/day/14
"""

__author__ = "Adam Karl"

INPUT_FILE = 'polymerization.txt'

class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None 
        
def printLinkedList(head):
    """Given the head of a linked list, print entire list"""
    curr = head
    while curr != None:
        print(curr.data, end='')
        curr = curr.next
    print('\n', flush=True)

def growPolymer():
    """Apply 10 steps of polymerization rules to the polymer and 
    return the frequency of the most used char minus the freq of the
    least used"""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    # clean input
    for i in range(len(input)):
        input[i] = input[i].strip()
    
    # read polymer into singly linked list
    polymer = input[0]
    head = None 
    for c in list(polymer)[::-1]:
        tmp = Node(c)
        tmp.next = head
        head = tmp
    
    # read rules into dictionary
    ruleDict = {}
    for line in input[2:]:
        pair, insert = line.split(' -> ')
        ruleDict[pair] = insert
        
        
    # printLinkedList(head)

    # simulate 10 steps
    for _ in range(10):
        curr = head 
        while curr.next != None:
            pair = curr.data + curr.next.data
            if pair in ruleDict:
                # add node between this one and next based on rule
                tmp = Node(ruleDict[pair])
                tmp.next = curr.next 
                curr.next = tmp 
                curr = tmp # to skip over inserted one
            curr = curr.next
        # printLinkedList(head)
        
    # count frequencies of each char
    freqDict = {}
    curr = head 
    while curr != None:
        c = curr.data
        if c in freqDict:
            freqDict[c] = freqDict[c] + 1
        else:
            freqDict[c] = 1
        curr = curr.next 
        
    maxFreq = max(freqDict.values())
    minFreq = min(freqDict.values())
    
    return maxFreq - minFreq
    

def main():    
    n = growPolymer()
    print(f"After 10 steps, the most used char is used {n} more times than the least used char")

if __name__ == "__main__":
    main()