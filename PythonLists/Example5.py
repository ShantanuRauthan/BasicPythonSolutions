#Write a Python program to find the list of words that are longer than n from a given list of words

#Code:

a = ['The','Art','Of','Traversing']
num = int(input())
b=[]
for i in a:
  if len(i)>num:
    b.append(i)
print(b)
    
