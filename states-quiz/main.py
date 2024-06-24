from turtle import Screen, Turtle
import pandas

screen = Screen()
data = pandas.read_csv("50-states.csv")

# add an external shape, allows Turtle to recognize the image file as a valid shape that can be assigned to a turtle
image = "./image/state_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

all_answers = True
nums_of_correct_ans = 0

def processing_the_answer(answer_state, data):
        # modify global var
        global nums_of_correct_ans

        # if state exits
        # .title to capitalize first letter
        if answer_state.title() in data["state"].to_list():
            # show name of this state in right position
            t = Turtle()
            t.pu()
            t.hideturtle()
            choosen_row = data[data.state == answer_state.title()]
            t.goto(int(choosen_row.x.array[0]),int(choosen_row.y.array[0]))
            t.write(answer_state.title())
            nums_of_correct_ans += 1

while all_answers:
    answer_state = screen.textinput(title=f"{nums_of_correct_ans}/50 states correct",prompt="What's another state's name?, type 'Exit' to quit.")
    if answer_state.title() == "Exit":
        break

    processing_the_answer(answer_state,data)
    if nums_of_correct_ans == 50:
        all_answers = False
