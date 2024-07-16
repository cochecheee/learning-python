# from flask import Flask

# app = Flask(__name__)

# def make_bold(function):
#     pass

# def make_emphasis(function):
#     pass

# def make_underlined(function):
#     pass

# @app.route("/")
# def bye():
#     return '<b>Hello, World!!</b>'

# if __name__ == '__main__':
#     app.run(debug=True)

# advanced python decorators function
class User:
    def __init__(self,name):
        self.username = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(*args)
    return wrapper

@is_authenticated_decorator
def create_blog_post(user,title):
    print(f"This is {user.username}'s new blog post with {title}.")

new_user = User("Tien")
#1. when you call `create_blog_post(new_user)`, actually python call `wrapper(user1) `cuz `create_blog_post` is decorated by `is_authenticated_decorator`
#2. `wrapper(user1) ` user1 is not defined in `is_authenticated_decorator` so the arguments of `wrapper(user1)` should be args or kwargs
new_user.is_logged_in = True
create_blog_post(new_user,'hello world!')
