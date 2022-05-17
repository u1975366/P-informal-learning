hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
try:
    h = int(hours)
    r = float(rate)
except:
    print("typecasting")
if h > 40:
    # 1.5 times the hourly rate for hours worked above 40 hours
    # new hourly rate for hours > 40 is 1.5 * r
    # 45 hours means the new hourly rate only applies to 5 Hours
    # otherwise the rest will still be 40 * r
    pay = ((1.5 * r) * (h - 40)) + (40 * r)
else:
    pay = int(hours) * float(rate)
print("Pay:", pay)
