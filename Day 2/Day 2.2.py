# Advent of Code 2018
# Jayden Kerr
# Day 2
# Puzzle 2

# Import the Counter class from Collections

from collections import Counter

# Read in the file.

input = open('input.txt', 'r')
boxIDs = input.read().strip().splitlines()
input.close()

for i in boxIDs:
        for j in boxIDs:
            diffs = 0
            for idNum, char in enumerate(i):
                if char != j[idNum]:
                    diffs += 1
            if diffs == 1:
                answer = [char for idNum, char in enumerate(i) if j[idNum] == char]
                print(''.join(answer))
