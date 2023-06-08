# Write a Python program to count the number of strings from a given list of strings. 
# Provided, the string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

#Code:
a = ['abc', 'xyz', 'aba', '1221']
count=0
for i in a:
  if len(i)>=2 and i[0]==i[-1]:
    count+=1
  else:
    pass
print(count)  
