import time
def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("start_time")
        func()
        end_time = time.time()
        print("end_time")
        print(f"Time taken by a function {end_time-start_time}")

    return wrapper()

@time_decorator
def test_case_ui():
    print("add a function,time taken by this function")
    time.sleep(2)









