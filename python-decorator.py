import time

# syntax of python decorator function
def my_decorator_function(function):
    print("outer wrap function")
    def wrapper_function():
        print("do domething BEFORE trigger the function")
        time.sleep(2)
        function()
        time.sleep(2)
        print("do domething AFTER trigger the function")
    return wrapper_function

@my_decorator_function
def say_hello():
    print("hello")

say_hello()