import turtle
import time
from Snake import Snake 
from Food import Food
from Score import Score

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

segments = []

food = Food()

snake = Snake()

score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right , "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "a")
screen.onkey(snake.left, "s")
screen.onkey(snake.right , "d")
def quit():
    with open("High_Score.txt") as file:
        prev_high_score = int(file.read())

    if (score.high_score > prev_high_score):
        with open("High_Score.txt","w") as file:
            file.write(str(score.high_score))

    if (score.score > prev_high_score):
        with open("High_Score.txt","w") as file:
            file.write(str(score.score))
    turtle.bye()
screen.onkey(quit, "q")

while True:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        snake.extend()
        food.reposition()
        score.increase_score()
        
    if snake.head.xcor() < -280:
        snake.head.setx(280)
    elif snake.head.xcor() > 280:
        snake.head.setx(-280)
    elif snake.head.ycor() < -280:
        snake.head.sety(280)
    elif snake.head.ycor() > 280:
        snake.head.sety(-280)

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
    



screen.exitonclick