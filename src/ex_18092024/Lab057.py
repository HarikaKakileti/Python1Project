def sum_of_three_numbers(a,b,c=10):  # for c we assigned default value 10
    return a+b+c
result=sum_of_three_numbers(1,2)
print(result)



def sum_of_three_numbers(a,b=9,c=10):  # for b and c we assigned default value 9,10
    return a+b+c
result=sum_of_three_numbers(8)
print(result)



def sum_of_three_numbers(a=10,b=10,c=10):  # for a,b,c we assigned default value
    return a+b+c
result=sum_of_three_numbers()
print(result)

