# Advent of Code 2018
# Jayden Kerr
# Day 2
# Puzzle 2

# Read in the file, creates a set with all of the IDs as a new line.

ids = []

for line in open("input.txt"):
	ids.append(line)

for x in ids:
	for y in ids:
		differences = 0
		for i in range(len(x)):
			if x[i] != y[i]:
				differences += 1
		if differences == 1


	

