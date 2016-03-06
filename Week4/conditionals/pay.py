hrs = raw_input("Enter Hours:")
rt = raw_input("Enter Rate:")
worked = 0
rate = 0

# Check if input is valid, quit with error code 100 if it is not
try:
    worked = float(hrs)
    rate = float(rt)
except ValueError:
    print "Not a float value"
    quit(100)

# overtime settings
overtimeStart = 40
overtimePay = rate * 1.5

if hrs <= 40:
    pay = worked * rate
else:
    pay = overtimeStart * rate + (worked - overtimeStart) * overtimePay

print str(pay)
