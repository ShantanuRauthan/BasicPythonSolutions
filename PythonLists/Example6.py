#Write a Python function that takes two lists and returns True if they have at least one common member.

#Code:

a = ['The','Art','Of','Traversing']
c = ['No','Common','String','Of']

def comp():
  for i in a:
    for j in c:
      if i==j:
        return True
        
print(comp())
    
