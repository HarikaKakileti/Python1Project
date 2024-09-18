### Task #7

"""✅ Leap Year Checker:

![img_1.png](img_1.png)

Create a program that determines whether a given year is a leap year.

A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination. """



"""Divisible by 4
Any year that is evenly divisible by four is a leap year. For example, 1988, 1992, and 1996 are leap years.
Divisible by 100
However, years that are divisible by 100 are not leap years, unless they are also divisible by 400. For example, 1900 was not a leap year, but 2000"""

year = int(input("Enter the year"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year")
else:
    print("Not a leap year")

