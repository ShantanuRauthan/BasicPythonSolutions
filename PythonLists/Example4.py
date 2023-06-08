#Write a Python program to check if a list is empty or not.

#Preferred Code:
a = []
if not a:
    print("List is empty")
else:
    print("List not empty")
    
#################################################
 #Alternate Code:
a = []
try:
  b = a[0]
  print("List not empty")
except Exception as e:
  print("List is empty")
  

