def sum_of_three_numbers(a,b,c):
    return a+b+c


i = lambda a,b,c:a+b+c
print(i(1,2,3))




# program using lambda to print even or odd
even_odd =lambda i: "even" if i%2==0 else"odd"
print(even_odd(9))