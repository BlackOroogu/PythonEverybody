import sys

inString = raw_input("Got somethng to say?")

try:
    howMuch = int(inString)
except:
    print "No way"
    exit(100)

print "You said:", str(howMuch)
