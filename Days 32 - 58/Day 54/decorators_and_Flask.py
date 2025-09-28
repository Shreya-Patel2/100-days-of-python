from flask import Flask

app = Flask(__name__)


# def make_underline(function):
#     return f"<u>Good Afternoon</u>"

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_italic(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


@app.route('/')
@make_underlined
@make_italic
@make_bold
def hello_world():
    return ("<h1 style='text-align: center'>Hello!</h1>"
            "<p >This is a paragraph</p>"
            "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExanRxNjdpM2I2dXR6YmMxNnFxMzVkc2FzZW5iYjJlc2YyeDU4ZWpqMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohs7POB6lS8wn0rle/giphy.gif'>")


@app.route('/username/<name>')
def greet(name):
    return f"Hi {name}!"


@app.route('/directory/<path:path>')
def path(path):
    return f"This is your path: {path}!"


if __name__ == "__main__":
    app.run(debug=True)

# set FLASK_APP="hello".py
# flask --app "hello"run

# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function() # call it, so print outer
# #outer_function()
#
# inner_function()
# inner_function()
# outer_function()
# inner_function()


