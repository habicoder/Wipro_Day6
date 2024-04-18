# import RE module
import re
 
target_str = "My roll number is 25"
res = re.findall("\d", target_str)
# extract mathing value
print(res) 
# Output [2, 5]