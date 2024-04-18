
import re
txt = "The rain in Spain"
x = re.search("^The", txt)  #^ is used to match at the begining
if x:
  print("YES! We have a match!")
else:
  print("No match")