from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_italic(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route('/')
@make_italic
@make_bold
@make_underline
def home_page():
    return 'Hello World'

@app.route('/bye')
def bye():
    return 'Bye'

@app.route('/greet/<name>/<int:age>')
def greet_age(name, age):
    return f'<h2 style= "text-align: center">Hello {name.title()}, how are you?\nYou are {age} years old!</h2>' \
           f'<p style= "text-align: center">This is a paragraph</p>' \
           f'<img src= "https://media.giphy.com/media/H8iL56bXGjVE4/giphy.gif">'

#The <> brackets let us pass in a variable#
@app.route('/username/<user>')
def greet(user):
    return f"Hi {user}, how are you?"

if __name__ == "__main__":
    app.run(debug=True)


#########-Advanced Python decorator functions-#########
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post")


new_user = User("Eddie")
new_user.is_logged_in = False
create_blog_post(new_user)
