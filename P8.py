# Python3 program to validate passport
# number of India using regular expression
import re
 
# Function to validate the pin code
# of India.
 
 
def isValidPassportNo(string):
 
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
	print(isValidPassportNo(str1))
 
	# Test Case 2:
	str2 = "A0296457"
	print(isValidPassportNo(str2))
 
	# Test Case 3:
	str3 = "Q2096453"
	print(isValidPassportNo(str3))
 
	# Test Case 4:
	str4 = "12096457"
	print(isValidPassportNo(str4))
 
	# Test Case 5:
	str5 = "A209645704"
	print(isValidPassportNo(str5))
 
# This code is contributed by AnkitRai01