# understanding Decorators in python


def my_decorator(func):     #func place i am driving will be called

    def wrapper():
        print("Before")
        print("wear helmet")
        func()  # calling drive_bike
        print("After")
        print("secure drive")
    return wrapper()

@my_decorator
def drive_bike():
    print("i am driving")




# without decorator

def my_decorator(func):     #func place i am driving will be called

    def wrapper():
        print("Before")
        print("wear helmet")
        func()  # calling drive_bike
        print("After")
        print("secure drive")
    return wrapper()

def drive_bike():
    print("i am driving")
drive_bike()
