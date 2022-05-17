# EXERCISE 5: Write a program which prompts the user for a Celsius tem-
# perature, convert the temperature to Fahrenheit, and print out the
# converted temperature.

celsiusTemp = input('Enter Celsius Temp: ')
farenTemp = (float(celsiusTemp) * 1.8) + 32
print("Fahrenheit Temp:", farenTemp)
