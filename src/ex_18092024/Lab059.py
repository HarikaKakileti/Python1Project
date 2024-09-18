
def print_arguments(*args):  # *args means unlimited number of arguments
    # *args = multiple argument with no limit, -> list
    print(args[0])

# list = ["pramod", "amit", "lucky"]

print_arguments("pramod", "amit", "lucky")
print_arguments("amit", "lucky")
print_arguments("lucky")
print_arguments()     # it will throw error because -minimum 1 argument is important


