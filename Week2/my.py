# Simple text output
import sys

print(sys.version)
# Store string literal for latter use
theStr = "You should never underestimate the predictability of stupidity.\n"

# Get padding width for quote 'author'
padWidth = len(theStr)

# See if .rjust works with string literal
theOutput = theStr + "-- Bullet Tooth Tony".rjust(len(theStr))
# Print all
print(theOutput)
