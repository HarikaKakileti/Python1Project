
# Write a program to ask the user which browser he want to run automation
browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        if browser_name == "firefox":
            print("Hello Hello")
        print("Execute the firefox Code")
    case "chrome":
        print("Execute the Chrome Code")
    case "edge":
        print("Execute the Edge Code")
    case "safari":
        print("Execute the Safari Code")
    case _:
        print("Browser Not Found!")