# Target String one
import re
str1 = "Emma's luck numbers are 251 761 231 4513"
 
# pattern to find three consecutive digits
string_pattern = r"\d{3}"
 
# compile string pattern to re.Pattern object
regex_pattern = re.compile(string_pattern)
 
 
 
# find all the matches in string one
result = regex_pattern.findall(str1)
print(result)