import sys
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
num = []
for i in range(1, n):
   num.append(int(sys.argv[i]))
try:
 print("sum: ", sum(num))
 print("Average: ", sum(num)/len(num))
except ZeroDivisionError:
 print("Error: divison by not zero ", )
