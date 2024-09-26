def add_before_ui_after_ui(func):
    def wrapper():
        print("Before the UI Test case")
        print("open browser")
        print(func)
        print("After the UI Test case")
        print("close browser")

    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print("I will test the Ui")



#----------------------

def add_before_ui_after_ui(custom_function_where_you_want_extra_func):
    # two parts
    # wrapper & call
    def wrapper():
        print("Before the running UI TC")
        print("Start the Browser ")
        custom_function_where_you_want_extra_func()
        print("Ending the running UI TC")
        print("Quit the Browser!")

    return wrapper()


@add_before_ui_after_ui
def test_ui():
    print("I will Test the UI")