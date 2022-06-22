#!/bin/python3

"""
Advent of Code 2021
Day 12 Part 1
https://adventofcode.com/2021/day/12
"""

__author__ = "Adam Karl"

INPUT_FILE = 'caveSystem.txt'

class graph:
    def __init__(self, dict=None):
        if dict is None:
            dict = {}
        self.graph_dict = dict 
        
    def addVertex(self, v):
        if v not in self.graph_dict:
            self.graph_dict[v] = []
            
    def addConnection(self, v0, v1):
        self.addVertex(v0)
        self.addVertex(v1)
        self.graph_dict[v0].append(v1)
        self.graph_dict[v1].append(v0)
        
    def getAllVertices(self):
        return self.graph_dict.keys()
        
    def getConnections(self, v):
        # return all vertices connected to this one
        return self.graph_dict[v]
    
    def __str__(self):
        ret = 'vertices\n'
        for v in self.graph_dict.keys():
            ret += v + ': '
            for c in self.getConnections(v):
                ret += c + ' '
            ret += '\n'
        return ret

def traverse(path, g):
    """Given a cave system graph and a list of caves visited so far, recursively
    try every possible next step and return the number of valid paths that
    reach this point"""
    curr = path[-1]
    
    if curr == 'end':
        # reached the end!
        print(path)
        return 1
    if len(path)>1 and curr == 'start':
        # returned to start => invalid path
        return 0
    if curr.islower() and curr in path[:-1]:
        # visited this small cave already => invalid path
        return 0
    
    paths = 0
    for next in g.getConnections(curr):
        newPath = path.copy()
        newPath.append(next)
        paths += traverse(newPath, g)
    return paths

def determineUniquePaths():
    """Read in the description of the cave system and determine the number
    of unique paths from start to end. Caves with capital letter names can
    be revisited, but caves with lowercase names can only be visited once."""
    
    f = open(INPUT_FILE, 'r')
    input = f.readlines()
    f.close()
    
    # build graph
    g = graph()
    for line in input:
        vertices = line.strip().split('-')
        g.addConnection(vertices[0], vertices[1])
        
    print(g)
       
    # use recursion to find all unique valid paths from start to end 
    totalPaths = traverse(['start'], g)
    return totalPaths

def main():    
    paths = determineUniquePaths()
    print(f"There are {paths} unique paths through the cave")

if __name__ == "__main__":
    main()