# Advent of Code 2018
# Jayden Kerr
# Day 1
# Puzzle 1

# Might come back to this - I need to save the session cookie once logged in order to cURL the contents of the page.
#import requests

#inputRequest = requests.get('https://adventofcode.com/2018/day/1/input')
#print(inputRequest.text)

puzzelInput = [int(x) for x in open("rawInput.txt").readlines()]
print(sum(puzzelInput))
