# Python3 program to validate the 
# pin code of India using Regular 

import re
 
# Function to validate the pin code
# of India. 
def isValidPinCode(pinCode):
	# Regex to check valid pin code
	# of India.
	regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$";
 
	# Compile the ReGex 
	p = re.compile(regex);
	
	if (pinCode == ''):
		return False;
	
	m = re.match(p, pinCode);
	
	if m is None:
		return False
	else:
		return True
 
# Driver code 
if __name__ == "__main__":
	# Test case 1
	num1 = "132103";
	print(num1, ": ", isValidPinCode(num1));
	# Test case 2:
	num2 = "201 305";
	print(num2, ": ", isValidPinCode(num2));
	# Test case 3:
	num3 = "014205";
	print(num3, ": ", isValidPinCode(num3));
	# Test case 4:
	num4 = "1473598";
	print(num4, ": ", isValidPinCode(num4));
