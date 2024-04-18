# To match American Express card numbers using a regular expression in Python, you can use the following pattern:
 
# Explanation:
 
# ^: Indicates the start of the string.
# 3: Matches the first digit of an American Express card number (which always starts with a 3).
# [0-9]{13}: Matches exactly 13 digits (the total length of an American Express card number).
# $: Indicates the end of the string.
 
# ===================================================
 
# visa card validation
 
 
# It should be 13 or 16 digits long, new cards have 16 digits and old cards have 13 digits.
# It should start with 4.
# If the cards have 13 digits the next twelve digits should be any number between 0-9.
# If the cards have 16 digits the next fifteen digits should be any number between 0-9.
# It should not contain any alphabet or special characters.
 
 
# ========================================================
 
# master card validation
 
# It should be 16 digits long.
# It should start with either two digits numbers may range from 51 to 55 or four digits numbers may range from 2221 to 2720.
# In the case of 51 to 55, the next fourteen digits should be any number between 0-9.
# In the case of 2221 to 2720, the next twelve digits should be any number between 0-9.
# It should not contain any alphabet or special characters.
 


 # Python3 program to validate passport
# number of India using regular expression
import re
 
# Function to validate the pin code
# of India.
 
 
def isValidAmerican(string):
 
	# Regex to check valid pin code
	# of India.
	regex = "^[A-PR-WY][1-9]\\d" +\
			"\\s?\\d{4}[1-9]$"
 
	# Compile the ReGex
	p = re.compile(regex)
 
	# If the string is empty
	# return false
	if (string == ''):
		return False
 
	# Pattern class contains matcher()
	# method to find matching between
	# given string and regular expression.
	m = re.match(p, string)
 
	# Return True if the string
	# matched the ReGex else False
	if m is None:
		return False
	else:
		return True
 
 
# Driver code.
if __name__ == "__main__":
 
	# Test Case 1
	str1 = "A21 90457"
	print(isValidAmerican(str1))
 
	# Test Case 2:
	str2 = "A0296457"
	print(isValidAmerican(str2))
 
	# Test Case 3:
	str3 = "Q2096453"
	print(isValidAmerican(str3))
 
	# Test Case 4:
	str4 = "12096457"
	print(isValidAmerican(str4))
 
	# Test Case 5:
	str5 = "A209645704"
	print(isValidAmerican(str5))
 


