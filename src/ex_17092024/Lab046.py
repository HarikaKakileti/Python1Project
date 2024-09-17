# Match Statement
# Switch in Java but in python we will call match
# match the output and execute
# Python > 3.10 in this version only match will be executed


#Syntax:
# match variable:
#     case pattern1:
#         # code block
#     case pattern2:
#         # code block

# Write a program to ask the user which browser he want to run automation
browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()   # if we given capital letters also it will convert to small letters for example :CHROME
match browser_name:
    case "firefox":
        print("Execute the firefox Code")
    case "chrome":
        print("Execute the Chrome Code")
    case "edge":
        print("Execute the Edge Code")
    case "safari":
        print("Execute the Safari Code")
    case _:
        print("Browser Not Found!")