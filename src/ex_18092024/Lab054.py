# 4 types of user defined functions
# 1.No return type and no parameter/argument
def greet():
    print("Hi world")
result=greet()
print(result)


#2.No return type with argument
def greet_by_name(name):
    print("hi" ,name)
greet_by_name("harika")

# 3. no return type with default argument
def say_hello_default_arg(name="harika"):  # if we don't pass anything harika will be taken default value
    print("hello",name)
say_hello_default_arg("kakileti")
say_hello_default_arg()
say_hello_default_arg(name ="Talli")  # positional argument



def multiple_args(name1="pavani",name2="satyavathi"):
    print("multiple_args", name1,name2)
multiple_args()



def multiple_args(name1="pavani",name2="satyavathi"):
    print("multiple_arguments", name1,name2)
multiple_args(name1="p",name2="S")



# 4.Argument+return type


def sum_of_two_numbers(num1,num2):
    return num1+num2
result = sum_of_two_numbers(10,20)
print(result)
