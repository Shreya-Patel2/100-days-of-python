import turtle
import pandas as pd
from names import Names

screen = turtle.Screen()
screen.title("US States Game")

image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pd.read_csv("./50_states.csv")
state = states_data["state"]
x_data = states_data["x"]
y_data = states_data["y"]

correct_states = []
for item in state:
    correct_states.append(item)

correct_guesses = []
answer_state = screen.textinput("Guess the State", "Name a state").title()
if answer_state in correct_states:
    correct_guesses.append(answer_state)
    x = int(x_data[state == answer_state].iloc[0])
    y = int(y_data[state == answer_state].iloc[0])
    display = Names(x, y, answer_state)
guesses = 49
while guesses <= 49:
    answer_state = screen.textinput(f"{guesses}/50 states left", "Name another state").title()
    if answer_state in correct_states:
        correct_guesses.append(answer_state)
        x = int(x_data[state == answer_state].iloc[0])
        y = int(y_data[state == answer_state].iloc[0])
        display = Names(x,y,answer_state)
        guesses -= 1

print(correct_guesses)
screen.exitonclick()