# import re
# #Check if the string starts with "The" and ends with "Spain":
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")


# Regex Functions
# findall	-> Returns a list containing all matches
# search	->  Returns a Match object if there is a match anywhere in the string
# split ->	Returns a list where the string has been split at each match
# sub ->	Replaces one or many matches with a string



import re
# txt = "The rain in Spain"
# #Find all lower case characters alphabetically between "a" and "m":
# x = re.findall("[a-m]", txt)
# print(x)


# txt = "Tha7t will be 59 dollars 76"
# x = re.findall('\d', txt)
# print(x)

# txt = "hello planet"
# x = re.findall("h...o",txt) # Search  for a sequence that starts with "he", followed by  two (any) characters,
# # and an "o":
# print(x)


# txt = "hello planet"

# # Check  if the  string started with 'hello'
# x = re.findall("^hello ", txt)
# if x:
#  print("Yes, the  string  starts with hello")
# else:
#  print("No match")


# text = "Hello Planet"
# # Check  if the string  ends with  'planet;
# x = re.findall("anet$", text)
# if x:
#  print("Yes, the string ends with 'planet' ")
# else:
#  print("Not Match")


# text = "hello planet"
# x = re.findall("he*o", text)
# print(x)

# define the pattern 
pattern = r"apple"
# Input strng 
text =  "I have  an apple and a banana"


#Use  re.search() to find  the pattern  in the text
match = re.search(pattern, text)

if match:
 print("Found 'apple' in the text")
else:
 print("Did not find 'apple' in the text.")
