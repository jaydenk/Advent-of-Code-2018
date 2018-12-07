# Advent of Code 2018
# Jayden Kerr
# Day 3
# Puzzle 1

import re

input = open('input.txt', 'r')
claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), input)
