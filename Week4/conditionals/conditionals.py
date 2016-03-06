import sys

inString = raw_input("Got somethng to say?")

try:
    howMuch = int(inString)
except ValueError:
    print "Not a number"
    exit(100)

print "You said:", inString
