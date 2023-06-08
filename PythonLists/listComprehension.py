#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']

#Code:
  
a = ['The','Art','Of','Traversing','elements','of','a','list']
mod_list = [x for (i,x) in enumerate(a) if i not in(0,4,5)]   #list comprehension

print(mod_list)
