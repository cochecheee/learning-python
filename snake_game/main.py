from turtle import Screen
import time
from snake import Snake

# set up screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
# stop the screen, when update it reload the screen
screen.tracer(0)

# create snake body
# each turtle should be a white square (20x20)
snake = Snake()
# starting_positions = [(0,0),(-20,0),(-40,0)]
# def create_snake_body():
#     """create body snake with 3 segments"""
#     for pos in starting_positions:
#         new_segment = Turtle(shape="square")
#         new_segment.color("white")
#         new_segment.pu()
#         new_segment.goto(pos)
#         snake.append(new_segment)
# create_snake_body()

# move the snake
game_is_on = True

# def move_snake():
#     """ move the snake follow the head """
#     for seg_num in range(len(snake)-1, 0, -1):
#         new_x = snake[seg_num-1].xcor()
#         new_y = snake[seg_num-1].ycor()
#         snake[seg_num].goto(new_x,new_y)
#     snake[0].forward(20)

# control snake (up down left right)
def listen_keyboard():
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")

while game_is_on:
    # update screen when all the segments move forward
    screen.update()
    listen_keyboard()
    # last to begin
    snake.move_snake()
    time.sleep(0.1)

# create food

# create scoreboard

# detect collision with wall

# detect collision with tail

# exit game
screen.exitonclick()