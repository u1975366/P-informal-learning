# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

while(1):
    hours = input('Enter Hours: ')
    rate = input('Enter Rate: ')
    try:
        h = int(hours)
        r = float(rate)
    except:
        print("Error, please enter numeric input")
        continue #  Use continue when you get bad input
    else:
        break # and break out of the loop when you're satisfied
if h > 40:
    pay = ((1.5 * r) * (h - 40)) + (40 * r)
else:
    pay = int(hours) * float(rate)
print("Pay:", pay)
