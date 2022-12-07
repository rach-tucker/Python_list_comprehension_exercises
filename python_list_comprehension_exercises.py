# Create a list of numbers that are less than ten using l_1 and list comprehension

l_1 = [1,11,14,5,8,9]

l_2 = [(num) for num in l_1 if num < 10]
print(l_2)


# Using list comprehension, create a list of names of 4 letters or more and capitalize each name

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']


names1_4 = [(name.title()) for name in names1 if (len(name)) >= 4 ]
print(names1_4)