#!/bin/python3

"""
Advent of Code 2021
Day 16 Part 1
https://adventofcode.com/2021/day/16
"""

__author__ = "Adam Karl"

INPUT_FILE = 'hexInput.txt'

def parseNextPacket(binaryString):
    """Parse the next packet of a binary input string.
    return the version number (if any), and the number of hex digits used"""
    packetVersion = int(binaryString[:3], 2)
    typeID = int(binaryString[3:6], 2)
    binaryString = binaryString[6:]
    
    versionSum = packetVersion
    if typeID == 4:
        # packet contains literal value
        literalValStr = ''
        while binaryString[0] == '1':
            # keep adding groups of 4b while leading bit is 1
            literalValStr += binaryString[1:5]
            binaryString = binaryString[5:]
            
        # leading bit is 0, this is last 4b to add to value
        literalValStr += binaryString[1:5]
        binaryString = binaryString[5:]
        
        # determine the literal value contained by the packet
        literalVal = int(literalValStr, 2)
        print(f'literal val {literalVal}')
        
    else:
        # packet contains operator
        lengthTypeID = binaryString[0]
        if lengthTypeID == '0':
            # next 15 bits represent length of sub-packets
            subPacketLen = int(binaryString[1:16], 2)
            binaryString = binaryString[16:]
            
            subPacket = binaryString[:subPacketLen]
            while len(subPacket) > 0:
                v, subPacket = parseNextPacket(subPacket)
                versionSum += v
            binaryString = binaryString[subPacketLen:]

        elif lengthTypeID == '1':
            # next 11 bits represent the number of sub-packets
            numSubPackets = int(binaryString[1: 12], 2)
            binaryString = binaryString[12:]
            
            for _ in range(numSubPackets):
                v, binaryString = parseNextPacket(binaryString)
                versionSum += v 

    print(f"Packet Version {packetVersion}, Type ID {typeID}: {versionSum}")
    return versionSum, binaryString

def parseHexInput():
    """Read in the hexadecimal input file and return the sum of all
    version numbers in the packets"""
    
    # read hexadecimal input
    f = open(INPUT_FILE, 'r')
    input = f.read().strip()
    f.close()
    
    # convert hex input to binary string, preserving leading 0s
    binaryString = bin(int(input, 16))[2:].zfill(len(input)*4)
    
    verSum, rem = parseNextPacket(binaryString)
    
    print(f"Remaining string: {rem}")

    return verSum

def main():    
    n = parseHexInput()
    print(f"The sum of all packet version numbers is {n}")

if __name__ == "__main__":
    main()
    