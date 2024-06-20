from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

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

# create food
food = Food()

# create score board
scoreboard = Scoreboard()

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

    # eat food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    # collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 \
            or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    
    # collision with tails
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()
            break

# exit game
screen.exitonclick()