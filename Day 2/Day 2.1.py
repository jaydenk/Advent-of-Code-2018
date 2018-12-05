# Advent of Code 2018
# Jayden Kerr
# Day 2
# Puzzle 1

numOfDoubles = 0
numOfTriples = 0

# Read in the file, creates a set with all of the characters in each line.

for line in open("input.txt"):
	charsInLine = set(line)
	isDouble = False
	isTriple = False
	
	# Iterates through each character, counting each time a given character is found. Sets the relavant boolean to True
	
	for char in charsInLine:
		count = line.count(char)
		if (count == 2):
			isDouble = True
		if (count == 3):
			isTriple = True
	
	# Takes that boolean and increments the count of each numOfDoubles and numOfTriples accordingly
	
	if (isDouble):
		numOfDoubles += 1
	if (isTriple):
		numOfTriples += 1
		
# Prints the resulting checksum

print(numOfDoubles * numOfTriples)
