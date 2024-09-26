# List : Collection of items(Duplicates is allowed)

my_list = [1,2,3]
print(my_list)
print(len(my_list))
print(my_list[1])
#print(my_list[10])

my_list[0] ="Harika"
my_list[1] ="Kakileti"
my_list[2] ="Harika"      # In list duplicates are allowed, it is like an array


#Indexing
print("element at the index 0",my_list[0])
print("element at the index 0",my_list[1])
print("element at the index 0",my_list[2])
print(my_list)


for element in my_list:
    print(element)


my_list =[1,2,3]
my_list.append(4)
my_list.append(5)  # Append object to the end of the list
my_list.append(6)  # Append object to the end of the list
print(my_list)




# append can take multiple times and while using append we can't add values at a time for example my_list.append(5,6,7)



# extend will be used to add multiple items
my_list= [10,11,12]
my_list.extend([13,14,15])
my_list.insert(0,"Venkata")   # insert will add element before the index
print(my_list)


my_list.insert(-1,"talli")    # It will add element in reverse manner ['Venkata', 10, 11, 12, 13, 14, 'talli', 15]
print(my_list)



#remove
my_list.remove("Venkata")
print(my_list)


#reverse
my_list.reverse()
print(my_list)

