# Simple text output
import sys

print(sys.version)
# Store string literal for latter use
theStr = "You should never underestimate the predictability of stupidity."

# Get padding width for quote 'author'
padWidth = len(theStr)

# Print all
print theStr, '\n', "-- Bullet Tooth Tony".rjust(len(theStr)-1)


# The code below almost works

name = raw_input("Enter your name")
print "Hello",ffname