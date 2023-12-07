import turtle

screen = turtle.Screen()
screen.bgcolor("white")
start_turtle = turtle.Turtle()
start_turtle.speed(2)

start_turtle.fillcolor("yellow")
start_turtle.begin_fill()

for _ in range(5):
    start_turtle.forward(100)
    start_turtle.right(144)

start_turtle.end_fill()
start_turtle.hideturtle()
turtle.done()