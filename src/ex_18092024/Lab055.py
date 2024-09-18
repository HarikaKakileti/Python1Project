# create a program to sum of three numbers from the user input

num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
num3=int(input("enter the number3"))
def sum_of_three_numbers(n1,n2,n3):
    return n1+n2+n3
result =sum_of_three_numbers(num1,num2,num3)
print(result)
result = sum_of_three_numbers(n1=num1,n2=num2,n3=num3)
print(result)

# 2nd type

num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
num3=int(input("enter the number3"))
def sum_of_three_numbers(n1,n2,n3):
    print(n1+n2+n3)
result =sum_of_three_numbers(num1,num2,num3)
print(result)
result = sum_of_three_numbers(n1=num1,n2=num2,n3=num3)
print(result)