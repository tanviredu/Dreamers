from turtle import *
speed(2)

## first we make the rectangle
## and the color will be green

begin_fill()
fillcolor("green")
for _ in range(2):
    forward(300)
    right(90)
    forward(200)
    right(90)
end_fill()

penup()
goto(150,-145)
pendown()
begin_fill()
fillcolor("red")
circle(50)
end_fill()

done()


from turtle import *

penup()
goto(-100,60)
pendown()
fillcolor("green")
begin_fill()
forward(300)
right(90)
forward(200)
right(90)
forward(300)
right(90)
forward(200)
hideturtle()
end_fill()

penup()
goto(110,-50)
pendown()
fillcolor("red")
begin_fill()
circle(50)
end_fill()
