#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
LastDigit = int(number) % 10
if LastDigit > 5 and LastDigit != 0:
	print("Last digit of " + str(number) + " is " + str(LastDigit) + " and is greater than 5 not 0")
elif LastDigit == 0:
	print("Last digit of " + str(number) + " is " + str(LastDigit) + " and is 0")
else:
	print("Last digit of " + str(number) + " is " + str(LastDigit) + " is less than 6 not 0")
