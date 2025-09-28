from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(1, 9)


@app.route('/')
def title():
    return ("<h1>Guess a number between 0 and 9!</h1>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2d6a2R6bWllMmFjZWdkdzYwa2hqZjJ4Znk3cDhlNnZ1czA2dTExOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ECdKlbACKs46YSk24H/giphy.gif'>")


@app.route(f'/<guessed_number>')
def number_guessed(guessed_number):
    if int(guessed_number) == random_number:
        return ("<h1 style='color:green;'>You guessed the number!</h1>"
                "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc29uanNlOGUzeWlkMjAyMzRlMmNtMWdjc3U3b2ZmbTJncjl6OTdoayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J1Pr1eMIHcyFeB4UrP/giphy.gif'>")

    elif int(guessed_number) > random_number:
        return ("<h1 style='color:purple;'>You guessed too high!</h1>"
                "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHhqbzEzdGh1M3p3eGkxaDZpNjJlNTZqamEzbWliOTY3ZG4wcndhMSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rwxuz6Via40ZcoPjfM/giphy.gif'>")

    else:
        return ("<h1 style='color:red;'>You guessed too low!</h1>"
                "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjJpd2h4NG1zOWRwbWxsanAycXVhODVxdm92anozY2J2bDZkY29tYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zjxIhGwrj6dk0O2lOL/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)
