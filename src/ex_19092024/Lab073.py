def my_decorator(func):     #func place i am driving will be called

    def wrapper():
        print("1.Before")
        print("2.wear helmet")
        func()  # calling drive_bike
        print("3.After")
        print("4.secure drive")
    return wrapper()
#@my_decorator
#def drive_bike():
   # print("i am driving")
@my_decorator
def drive_scooty():     # this is normal function if we want to give more secure we will use decorator in line 13
    print("normal function")


