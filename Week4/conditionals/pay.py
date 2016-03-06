hrs = raw_input("Enter Hours:")
worked = 0
# standard payment
rate = 10.5

# overtime settings
overtimeStart = 40
overtimePay = rate * 1.5

# Check if input is valid, quit with error code 100 if it is not
try:
    worked = float(hrs)
except ValueError:
    print "Not a float value"
    quit(100)

if hrs <= 40:
    pay = worked * rate
else:
    pay = overtimeStart * rate + (worked - overtimeStart) * overtimePay

print str(pay)
