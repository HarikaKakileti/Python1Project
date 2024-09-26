import math

def give_me_power(num):
    return math.pow(num,2)   # here value will be float that's why we are using o variable to store the data
o=give_me_power(3)
print(o)




# let's create above program using lambda and asking user for input

p=lambda : math.pow(int(input("enter the number")),2)
print(p())