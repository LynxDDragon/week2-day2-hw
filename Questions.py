#EXERCISE 1
#Given a list as a parameter,write a function that returns a list of numbers that are less than ten
#For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

l_1 = [1,11,14,5,8,9]

def less(num):
    less10 = []
    for n in num:
        if n < 10:
            less10.append(n)
    return less10
print(less(l_1))

#EXERCISE 2

#Write a function that takes in two lists and returns the two lists merged together and sorted
#Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def merge(list1, list2):
    merged = list1 + list2
    merged = set(merged)
    return merged
print(merge(l_1, l_2))

