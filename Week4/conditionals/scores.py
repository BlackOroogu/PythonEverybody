score = raw_input("Please enter Score: ")
theScore = 0.0
try:
    theScore = float(score)
except ValueError:
    print "ERROR: Value '{0}' is not a float number.".format(score)
    exit()

if theScore > 1.0 or theScore < 0.0:
    print "ERROR: Value '{0}' is out of range.\nAccepted values are in range [0.0 .. 1.0]".format(score)
    quit()

if theScore >= 0.9:
    strScore = 'A'
elif theScore >= 0.8:
    strScore = 'B'
elif theScore >= 0.7:
    strScore = 'C'
elif theScore >= 0.6:
    strScore = 'D'
else:
    strScore = 'F'

print strScore

