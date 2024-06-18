from turtle import Turtle, Screen
import random

screen = Screen()
# set up the screen
screen.setup(width=500,height=400)

# guess the turtle will be win
is_race_on = False
user_guess = screen.textinput(title="Make a bet",prompt="Which turtle will win the race? Enter the color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# random value for each turtle to go forward
def go_forward(turtle, speed):
    turtle.fd(speed)

# list of turtle
list_of_turtles = []
# initalize some turtle with their color
def create_turtle():
    for i in range(6):
        my_turtle = Turtle(shape="turtle")
        my_turtle.color(colors[i])
        # turn off the pen
        my_turtle.pu()
        # go to a position(x,y)
        my_turtle.goto(x=-230,y=y_positions[i])
        list_of_turtles.append(my_turtle)

def start_game():
    if user_guess:
        is_race_on = True
    while is_race_on:
        for turtle in list_of_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_guess:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
            rand_speed = random.randint(0,10)
            go_forward(turtle=turtle,speed=rand_speed)


create_turtle()
start_game()



# exit the game
screen.exitonclick()