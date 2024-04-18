# Create a function StringBinaryOperations()
# The Binary number system uses two digits 0 and 1 and number system can be called binary 
# string. You are required to implement given function
 
# StringBinaryOperations() This function accepts a string str as its argument. The string str 
# consists of binary digits separated with an alphabet as follows:
 
# - X denotes AND operation
# - Y denotes OR operation
# - Z denotes XOR Operation
 
# 0 and 0 = 0
# 1 and 0 = 0
# 0 and 1 = 0
# 1 and 1 = 1
 
# 0 or 0 = 0
# 1 or 0 = 1
# 0 or 1 = 1
# 1 or 1 = 1
 
#   XOR
 
#   0 xor 0 = 0
#   1 xor 0 = 1
#   0 xor 1 = 1
#   1 xor 1 = 0
 


 
# You are required to calculate the result of the string, scanning the string to right taking one 
# operation at a time, and return the same.
# Note:
# • No order of priorities of operations is required
# • Length of str is odd
# • If str is NULL / None (in case of Python), return “Invalid Input”
# Input str: 1Z0Z1Z1X0Y1
# Output: 1

# &	Bitwise AND	x & y = 0 (0000 0000)
# |	Bitwise OR	x | y = 14 (0000 1110)
# ~	Bitwise NOT	~x = -11 (1111 0101)
# ^	Bitwise XOR	x ^ y = 14 (0000 1110)

def StringBinaryOperation(str):
    if str is None or len(str) ==0:
        return 'Invalid Input'
    result=int(str[0])
    i=1
    while i<len(str):
        if str[i]=='X':
            result &= int(str[i+1])
        elif str[i]=='Y':
            result|=int(str[i+1])
        elif str[i]=='Z':
            result^=int(str[i+1])
        i+=2
    return result
str='1Z0Z1Z1X0Y1'
print(StringBinaryOperation(str))

