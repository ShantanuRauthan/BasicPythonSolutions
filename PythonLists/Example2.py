#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

#Code:
a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(a, key = lambda x:x[-1]))


#Explanation
#Yeah a two liner code lol
#We basically sorted the list having tuples but with respect to the last element using the lambda function provided as key parameter.
