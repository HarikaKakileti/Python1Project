a,b,c =(1,2,3)
print(a)
print(b)
print(c)



#search in tuple

cities = ("london","tokyo","paris")
print("paris" in cities)
print("Delhi" in cities)

t =(1,2,3)
#t.append(4)
my_list = list(t) #tuple object has no attribute
my_list.append(4)
t=tuple(my_list)
print(t)
print(my_list)