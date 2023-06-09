#Write a Python program to find the second largest number in a list.

#Code:

list1 = [1,4,3,5]
a = max(list1)
list1.remove(a)
print(max(list1))


#Alternative Code:

list1 = [1,4,3,5]
a = sorted(list1)
print(a[-2])

  

  

  

  
