#Check if two lists are circularly identical
#circularly identical = two list with same elements positioned differently


#Code:

list1 = [1,4,3,5]
list2 = [4,3,5,7]

if len(list1)==len(list2):
  for i in list2:
    list1.append(i)
  
  if len(list2)==len(set(list1)):
    print("Circulary Identical")
  else:
    print("Not identical")
  
else:
  print("Not identical")


  

  
