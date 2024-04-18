import re
str1 = "Emma's luck numbers are 251 761 231 45"
string_pattern = r"\d{3}"
regex_pattern = re.compile(string_pattern)
result = regex_pattern.findall(str1)
print(result)