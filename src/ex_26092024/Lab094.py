# SET is a collection of unique elements
#{}

list_of_unique_items = {1,2,3}
print(list_of_unique_items)


list = [11,11,12,13]
s = set(list)
print(s)




set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
my_set = set1.intersection(set2)
print(my_set)
#my_set = set2.difference(set1)
my_set = set1.difference(set2)
print(my_set)




set1 = {1,2,3,4,5}
set2 = {1,2,3,7,8}
subset = set2.issubset(set1)
subset = set1.issubset(set2)  # if all the elements are matched then it return true
print(subset)


set1 = {1,2,3,4,5}
set2 = {1,2,3,4,5}
subset = set2.issubset(set1)
subset = set1.issubset(set2)  # if all the elements are matched then it return true
print(subset)




